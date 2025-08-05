"""
Form handler for Form Bot
Handles web form interaction using Selenium WebDriver
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from typing import Dict, Optional
import config
from .logger import Logger

class FormHandler:
    """Handles web form interaction and submission"""
    
    def __init__(self):
        self.logger = Logger()
        self.driver = None
        self.wait = None
    
    def setup_driver(self):
        """Setup Chrome WebDriver with configuration"""
        try:
            self.logger.info("Setting up Chrome WebDriver...")
            
            # Chrome options
            chrome_options = Options()
            if config.BROWSER_CONFIG['headless']:
                chrome_options.add_argument('--headless')
            
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument(f'--window-size={config.BROWSER_CONFIG["window_size"][0]},{config.BROWSER_CONFIG["window_size"][1]}')
            chrome_options.add_argument(f'--user-agent={config.BROWSER_CONFIG["user_agent"]}')
            
            # Setup service with automatic ChromeDriver management
            service = Service(ChromeDriverManager().install())
            
            # Create driver
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.implicitly_wait(config.TIMING['implicit_wait'])
            self.driver.set_page_load_timeout(config.TIMING['page_load_timeout'])
            
            # Setup explicit wait
            self.wait = WebDriverWait(self.driver, config.TIMING['element_wait_timeout'])
            
            self.logger.success("Chrome WebDriver setup completed")
            
        except Exception as e:
            self.logger.error(f"Failed to setup Chrome WebDriver: {str(e)}")
            raise
    
    def navigate_to_form(self, url: str = None):
        """
        Navigate to the form page
        
        Args:
            url: Form URL (uses config default if None)
        """
        if url is None:
            url = config.FORM_URL
        
        try:
            self.logger.info(f"Navigating to form: {url}")
            self.driver.get(url)
            
            # Wait for page to load
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            self.logger.success("Successfully navigated to form page")
            
        except TimeoutException:
            self.logger.error("Timeout while loading form page")
            raise
        except Exception as e:
            self.logger.error(f"Error navigating to form: {str(e)}")
            raise
    
    def fill_form(self, data: Dict[str, str]) -> bool:
        """
        Fill form with provided data
        
        Args:
            data: Dictionary with field names and values
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info(f"Filling form for: {data.get('name', 'Unknown')}")
            
            # Fill name field
            if 'name' in data and data['name']:
                self._fill_field('name', data['name'])
            
            # Fill email field
            if 'email' in data and data['email']:
                self._fill_field('email', data['email'])
            
            # Fill subject field
            if 'subject' in data and data['subject']:
                self._fill_field('subject', data['subject'])
            
            # Fill message field
            if 'message' in data and data['message']:
                self._fill_field('message', data['message'])
            
            # Check consent checkbox
            self._check_consent()
            
            self.logger.success("Form filled successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error filling form: {str(e)}")
            return False
    
    def _fill_field(self, field_name: str, value: str):
        """Fill a specific form field"""
        try:
            xpath = config.FORM_FIELDS.get(field_name)
            if not xpath:
                self.logger.warning(f"No XPath configured for field: {field_name}")
                return
            
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.clear()
            element.send_keys(value)
            self.logger.debug(f"Filled {field_name} field")
            
        except TimeoutException:
            self.logger.error(f"Timeout waiting for {field_name} field")
            raise
        except Exception as e:
            self.logger.error(f"Error filling {field_name} field: {str(e)}")
            raise
    
    def _check_consent(self):
        """Check the consent checkbox"""
        try:
            xpath = config.FORM_FIELDS.get('consent')
            if not xpath:
                self.logger.warning("No consent checkbox configured")
                return
            
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not element.is_selected():
                self.driver.execute_script("arguments[0].click();", element)
                self.logger.debug("Consent checkbox checked")
            
        except TimeoutException:
            self.logger.error("Timeout waiting for consent checkbox")
            raise
        except Exception as e:
            self.logger.error(f"Error checking consent: {str(e)}")
            raise
    
    def submit_form(self) -> bool:
        """
        Submit the form
        
        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info("Submitting form...")
            
            xpath = config.FORM_FIELDS.get('submit')
            if not xpath:
                self.logger.error("No submit button configured")
                return False
            
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].click();", submit_button)
            
            # Wait a moment for submission
            time.sleep(2)
            
            self.logger.success("Form submitted successfully")
            return True
            
        except TimeoutException:
            self.logger.error("Timeout waiting for submit button")
            return False
        except Exception as e:
            self.logger.error(f"Error submitting form: {str(e)}")
            return False
    
    def wait_between_submissions(self):
        """Wait between form submissions"""
        delay = config.TIMING['delay_between_submissions']
        self.logger.debug(f"Waiting {delay} seconds before next submission...")
        time.sleep(delay)
    
    def close_driver(self):
        """Close the WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("WebDriver closed")
            except Exception as e:
                self.logger.warning(f"Error closing WebDriver: {str(e)}")
    
    def get_page_title(self) -> str:
        """Get current page title"""
        return self.driver.title if self.driver else ""
    
    def take_screenshot(self, filename: str = None):
        """Take a screenshot of the current page"""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        
        try:
            self.driver.save_screenshot(f"logs/{filename}")
            self.logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            self.logger.warning(f"Failed to take screenshot: {str(e)}") 
"""
Configuration file for Form Bot
Contains all configurable settings for the automated form submission tool
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Form Configuration
FORM_URL = os.getenv('FORM_URL', 'http://localhost:8000')
EXCEL_FILE = os.getenv('EXCEL_FILE', 'data/sample_data.xlsx')

# Form Field Mappings (XPath selectors)
FORM_FIELDS = {
    'name': '//*[@id="jform_contact_name"]',
    'email': '//*[@id="jform_contact_email"]',
    'subject': '//*[@id="jform_contact_emailmsg"]',
    'message': '//*[@id="jform_contact_message"]',
    'consent': '//*[@id="jform_consentbox0"]',
    'submit': '//*[@id="contact-form"]/div/div/button'
}

# Excel Column Mappings
EXCEL_COLUMNS = {
    'name': 'Nome',
    'email': 'Email',
    'subject': 'Assunto',
    'message': 'Mensagem'
}

# Timing Configuration (in seconds)
TIMING = {
    'page_load_timeout': 30,
    'element_wait_timeout': 10,
    'delay_between_submissions': 2,
    'implicit_wait': 5
}

# Browser Configuration
BROWSER_CONFIG = {
    'headless': False,  # Set to True for headless mode
    'window_size': (1920, 1080),
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Logging Configuration
LOGGING = {
    'level': 'INFO',
    'file': 'logs/form_bot.log',
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# Error Handling
ERROR_HANDLING = {
    'max_retries': 3,
    'retry_delay': 5,
    'continue_on_error': True
} 
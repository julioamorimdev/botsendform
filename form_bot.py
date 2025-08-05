"""
Main Form Bot class
Orchestrates the automated form submission process
"""

import time
from typing import Optional
from utils.excel_reader import ExcelReader
from utils.form_handler import FormHandler
from utils.logger import Logger
import config

class FormBot:
    """Main bot class for automated form submission"""
    
    def __init__(self):
        self.logger = Logger()
        self.excel_reader = ExcelReader()
        self.form_handler = FormHandler()
        self.stats = {
            'total_rows': 0,
            'processed': 0,
            'successful': 0,
            'failed': 0,
            'start_time': None,
            'end_time': None
        }
    
    def run(self, excel_file: str = None, form_url: str = None):
        """
        Run the complete form submission process
        
        Args:
            excel_file: Path to Excel file (uses config default if None)
            form_url: Form URL (uses config default if None)
        """
        try:
            self.stats['start_time'] = time.time()
            self.logger.info("Starting Form Bot...")
            
            # Read Excel data
            self._read_excel_data(excel_file)
            
            # Setup browser
            self._setup_browser()
            
            # Process each row
            self._process_all_rows(form_url)
            
            # Finalize
            self._finalize()
            
        except Exception as e:
            self.logger.error(f"Critical error in Form Bot: {str(e)}")
            self._finalize()
            raise
    
    def _read_excel_data(self, excel_file: str = None):
        """Read and validate Excel data"""
        try:
            self.excel_reader.read_file(excel_file)
            self.stats['total_rows'] = self.excel_reader.get_total_rows()
            
            if self.stats['total_rows'] == 0:
                raise ValueError("No valid data found in Excel file")
            
            self.logger.info(f"Found {self.stats['total_rows']} rows to process")
            self.excel_reader.display_sample(3)  # Show first 3 rows
            
        except Exception as e:
            self.logger.error(f"Failed to read Excel data: {str(e)}")
            raise
    
    def _setup_browser(self):
        """Setup browser for form submission"""
        try:
            self.form_handler.setup_driver()
        except Exception as e:
            self.logger.error(f"Failed to setup browser: {str(e)}")
            raise
    
    def _process_all_rows(self, form_url: str = None):
        """Process all rows in the Excel file"""
        for i in range(self.stats['total_rows']):
            try:
                self.stats['processed'] += 1
                self.logger.progress(self.stats['processed'], self.stats['total_rows'], "Processing forms")
                
                # Get data for current row
                row_data = self.excel_reader.get_data_for_row(i)
                
                # Process single row
                success = self._process_single_row(row_data, form_url)
                
                if success:
                    self.stats['successful'] += 1
                else:
                    self.stats['failed'] += 1
                
                # Wait between submissions
                if i < self.stats['total_rows'] - 1:  # Don't wait after last submission
                    self.form_handler.wait_between_submissions()
                
            except Exception as e:
                self.logger.error(f"Error processing row {i + 1}: {str(e)}")
                self.stats['failed'] += 1
                
                if not config.ERROR_HANDLING['continue_on_error']:
                    raise
    
    def _process_single_row(self, row_data: dict, form_url: str = None) -> bool:
        """
        Process a single row of data
        
        Args:
            row_data: Dictionary with form data
            form_url: Form URL to submit to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Navigate to form
            self.form_handler.navigate_to_form(form_url)
            
            # Fill form
            if not self.form_handler.fill_form(row_data):
                return False
            
            # Submit form
            if not self.form_handler.submit_form():
                return False
            
            self.logger.success(f"Successfully processed: {row_data.get('name', 'Unknown')}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to process row: {str(e)}")
            return False
    
    def _finalize(self):
        """Finalize the bot execution"""
        try:
            # Close browser
            self.form_handler.close_driver()
            
            # Calculate statistics
            self.stats['end_time'] = time.time()
            duration = self.stats['end_time'] - self.stats['start_time']
            
            # Display final statistics
            self._display_final_stats(duration)
            
        except Exception as e:
            self.logger.warning(f"Error during finalization: {str(e)}")
    
    def _display_final_stats(self, duration: float):
        """Display final execution statistics"""
        self.logger.info("=" * 50)
        self.logger.info("EXECUTION COMPLETED")
        self.logger.info("=" * 50)
        self.logger.info(f"Total rows: {self.stats['total_rows']}")
        self.logger.info(f"Processed: {self.stats['processed']}")
        self.logger.info(f"Successful: {self.stats['successful']}")
        self.logger.info(f"Failed: {self.stats['failed']}")
        self.logger.info(f"Success rate: {(self.stats['successful'] / self.stats['total_rows'] * 100):.1f}%")
        self.logger.info(f"Duration: {duration:.2f} seconds")
        self.logger.info("=" * 50)
    
    def get_stats(self) -> dict:
        """Get current execution statistics"""
        return self.stats.copy()
    
    def reset_stats(self):
        """Reset execution statistics"""
        self.stats = {
            'total_rows': 0,
            'processed': 0,
            'successful': 0,
            'failed': 0,
            'start_time': None,
            'end_time': None
        } 
"""
Excel file reader for Form Bot
Handles reading and validating Excel files with contact data
"""

import pandas as pd
import os
from typing import Dict, List, Optional
import config
from .logger import Logger

class ExcelReader:
    """Handles Excel file reading and data validation"""
    
    def __init__(self):
        self.logger = Logger()
        self.data = None
        self.required_columns = list(config.EXCEL_COLUMNS.values())
    
    def read_file(self, file_path: str = None) -> pd.DataFrame:
        """
        Read Excel file and validate data
        
        Args:
            file_path: Path to Excel file (uses config default if None)
            
        Returns:
            pandas DataFrame with validated data
            
        Raises:
            FileNotFoundError: If Excel file doesn't exist
            ValueError: If required columns are missing
        """
        if file_path is None:
            file_path = config.EXCEL_FILE
        
        # Check if file exists
        if not os.path.exists(file_path):
            self.logger.error(f"Excel file not found: {file_path}")
            raise FileNotFoundError(f"Excel file not found: {file_path}")
        
        try:
            self.logger.info(f"Reading Excel file: {file_path}")
            self.data = pd.read_excel(file_path)
            self.logger.success(f"Successfully read {len(self.data)} rows from Excel file")
            
            # Validate data
            self._validate_data()
            
            return self.data
            
        except Exception as e:
            self.logger.error(f"Error reading Excel file: {str(e)}")
            raise
    
    def _validate_data(self):
        """Validate Excel data structure and content"""
        if self.data is None:
            raise ValueError("No data loaded")
        
        # Check required columns
        missing_columns = []
        for column in self.required_columns:
            if column not in self.data.columns:
                missing_columns.append(column)
        
        if missing_columns:
            self.logger.error(f"Missing required columns: {missing_columns}")
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # Check for empty data
        if len(self.data) == 0:
            self.logger.warning("Excel file is empty")
            return
        
        # Validate email format
        self._validate_emails()
        
        # Remove rows with empty required fields
        self._clean_data()
        
        self.logger.info(f"Data validation completed. {len(self.data)} valid rows found")
    
    def _validate_emails(self):
        """Validate email format"""
        email_column = config.EXCEL_COLUMNS['email']
        invalid_emails = []
        
        for index, email in enumerate(self.data[email_column]):
            if pd.isna(email) or not self._is_valid_email(str(email)):
                invalid_emails.append((index + 1, email))
        
        if invalid_emails:
            self.logger.warning(f"Found {len(invalid_emails)} invalid emails")
            for row, email in invalid_emails[:5]:  # Show first 5
                self.logger.warning(f"Row {row}: Invalid email '{email}'")
    
    def _is_valid_email(self, email: str) -> bool:
        """Simple email validation"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _clean_data(self):
        """Remove rows with empty required fields"""
        initial_count = len(self.data)
        
        # Remove rows where any required column is empty
        for column in self.required_columns:
            self.data = self.data.dropna(subset=[column])
        
        removed_count = initial_count - len(self.data)
        if removed_count > 0:
            self.logger.warning(f"Removed {removed_count} rows with empty required fields")
    
    def get_data_for_row(self, index: int) -> Dict[str, str]:
        """
        Get data for a specific row
        
        Args:
            index: Row index
            
        Returns:
            Dictionary with field names and values
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if index >= len(self.data):
            raise IndexError(f"Row index {index} out of range")
        
        row_data = {}
        for field, column in config.EXCEL_COLUMNS.items():
            value = self.data.iloc[index][column]
            row_data[field] = str(value) if pd.notna(value) else ""
        
        return row_data
    
    def get_total_rows(self) -> int:
        """Get total number of rows"""
        return len(self.data) if self.data is not None else 0
    
    def display_sample(self, rows: int = 5):
        """Display sample data for verification"""
        if self.data is None:
            self.logger.warning("No data loaded")
            return
        
        self.logger.info("Sample data from Excel file:")
        print(self.data.head(rows).to_string(index=False)) 
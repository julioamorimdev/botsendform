"""
Logging utilities for Form Bot
Provides comprehensive logging functionality with file and console output
"""

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from colorama import Fore, Style, init
import config

# Initialize colorama for colored console output
init(autoreset=True)

class Logger:
    """Enhanced logger with colored console output and file logging"""
    
    def __init__(self, name='FormBot'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, config.LOGGING['level']))
        
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup file and console handlers"""
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # File handler with rotation
        file_handler = RotatingFileHandler(
            config.LOGGING['file'],
            maxBytes=config.LOGGING['max_file_size'],
            backupCount=config.LOGGING['backup_count']
        )
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # Console handler with colors
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """Log info message with green color"""
        colored_message = f"{Fore.GREEN}[INFO]{Style.RESET_ALL} {message}"
        self.logger.info(colored_message)
    
    def warning(self, message):
        """Log warning message with yellow color"""
        colored_message = f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}"
        self.logger.warning(colored_message)
    
    def error(self, message):
        """Log error message with red color"""
        colored_message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}"
        self.logger.error(colored_message)
    
    def success(self, message):
        """Log success message with bright green color"""
        colored_message = f"{Fore.LIGHTGREEN_EX}[SUCCESS]{Style.RESET_ALL} {message}"
        self.logger.info(colored_message)
    
    def progress(self, current, total, description="Processing"):
        """Log progress with percentage"""
        percentage = (current / total) * 100
        colored_message = f"{Fore.CYAN}[PROGRESS]{Style.RESET_ALL} {description}: {current}/{total} ({percentage:.1f}%)"
        self.logger.info(colored_message)
    
    def debug(self, message):
        """Log debug message with blue color"""
        colored_message = f"{Fore.BLUE}[DEBUG]{Style.RESET_ALL} {message}"
        self.logger.debug(colored_message) 
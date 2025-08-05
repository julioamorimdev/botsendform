"""
Main entry point for Form Bot
Provides command-line interface and main execution logic
"""

import sys
import argparse
from form_bot import FormBot
from utils.logger import Logger
import config

def main():
    """Main function with command-line argument parsing"""
    parser = argparse.ArgumentParser(
        description="Form Bot - Automated Form Submission Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                                    # Use default configuration
  python main.py --excel data.xlsx                  # Use specific Excel file
  python main.py --url http://example.com/form     # Use specific form URL
  python main.py --excel data.xlsx --url http://example.com/form
        """
    )
    
    parser.add_argument(
        '--excel', '-e',
        type=str,
        help='Path to Excel file (default: from config)'
    )
    
    parser.add_argument(
        '--url', '-u',
        type=str,
        help='Form URL (default: from config)'
    )
    
    parser.add_argument(
        '--headless', '-H',
        action='store_true',
        help='Run browser in headless mode'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Read Excel file and validate data without submitting forms'
    )
    
    args = parser.parse_args()
    
    # Setup logger
    logger = Logger()
    
    # Display welcome message
    logger.info("=" * 60)
    logger.info("FORM BOT - Automated Form Submission Tool")
    logger.info("=" * 60)
    logger.info("Educational use only - Do not use for commercial purposes")
    logger.info("=" * 60)
    
    try:
        # Update configuration based on arguments
        if args.headless:
            config.BROWSER_CONFIG['headless'] = True
            logger.info("Running in headless mode")
        
        if args.verbose:
            config.LOGGING['level'] = 'DEBUG'
            logger.info("Verbose logging enabled")
        
        # Create and run bot
        bot = FormBot()
        
        if args.dry_run:
            logger.info("DRY RUN MODE - No forms will be submitted")
            _run_dry_run(bot, args.excel)
        else:
            bot.run(excel_file=args.excel, form_url=args.url)
        
        logger.success("Form Bot execution completed successfully!")
        
    except KeyboardInterrupt:
        logger.warning("Execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        sys.exit(1)

def _run_dry_run(bot: FormBot, excel_file: str = None):
    """Run bot in dry-run mode (only read and validate data)"""
    logger = Logger()
    
    try:
        # Read Excel data
        bot.excel_reader.read_file(excel_file)
        total_rows = bot.excel_reader.get_total_rows()
        
        logger.info(f"DRY RUN: Found {total_rows} rows in Excel file")
        logger.info("DRY RUN: Data validation completed successfully")
        logger.info("DRY RUN: No forms were submitted")
        
        # Display sample data
        bot.excel_reader.display_sample(5)
        
    except Exception as e:
        logger.error(f"DRY RUN failed: {str(e)}")
        raise

if __name__ == "__main__":
    main() 
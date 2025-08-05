#!/usr/bin/env python3
"""
Form Bot Demo Script
Demonstrates how to use the Form Bot with a simple example
"""

from form_bot import FormBot
from utils.logger import Logger

def demo_basic_usage():
    """Demonstrate basic usage of Form Bot"""
    logger = Logger()
    
    logger.info("=" * 60)
    logger.info("FORM BOT - DEMONSTRAÇÃO")
    logger.info("=" * 60)
    
    # Create bot instance
    bot = FormBot()
    
    try:
        # Run the bot with test data
        logger.info("Iniciando demonstração...")
        bot.run(
            excel_file="data/sample_data.xlsx",
            form_url="http://localhost:8000/test_form.html"
        )
        
        # Show statistics
        stats = bot.get_stats()
        logger.success("Demonstração concluída com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro na demonstração: {str(e)}")
        logger.info("Certifique-se de que:")
        logger.info("1. O servidor de teste está rodando (python test/test_server.py)")
        logger.info("2. Os dados de exemplo foram criados (python create_sample_data.py)")

def demo_dry_run():
    """Demonstrate dry run mode"""
    logger = Logger()
    
    logger.info("=" * 60)
    logger.info("FORM BOT - DEMO DRY RUN")
    logger.info("=" * 60)
    
    # Create bot instance
    bot = FormBot()
    
    try:
        # Read and validate data without submitting forms
        logger.info("Executando validação de dados...")
        bot.excel_reader.read_file("data/sample_data.xlsx")
        
        total_rows = bot.excel_reader.get_total_rows()
        logger.success(f"Encontrados {total_rows} registros válidos")
        
        # Show sample data
        bot.excel_reader.display_sample(3)
        
        logger.info("Validação concluída - nenhum formulário foi enviado")
        
    except Exception as e:
        logger.error(f"Erro na validação: {str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        demo_dry_run()
    else:
        demo_basic_usage() 
#!/usr/bin/env python3
"""
Quick Start Script for Form Bot
Helps users get started quickly with the Form Bot
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("🚀 FORM BOT - QUICK START")
    print("=" * 60)
    print("Este script irá ajudá-lo a configurar o Form Bot rapidamente")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Erro: Python 3.7 ou superior é necessário")
        print(f"   Versão atual: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} - OK")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        return False

def create_sample_data():
    """Create sample Excel data"""
    print("\n📊 Criando dados de exemplo...")
    try:
        subprocess.check_call([sys.executable, "create_sample_data.py"])
        print("✅ Dados de exemplo criados")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao criar dados de exemplo")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Criando diretórios necessários...")
    directories = ['logs', 'data']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Diretórios criados")

def show_next_steps():
    """Show next steps to the user"""
    print("\n" + "=" * 60)
    print("🎉 CONFIGURAÇÃO CONCLUÍDA!")
    print("=" * 60)
    print("\n📋 Próximos passos:")
    print("1. Inicie o servidor de teste:")
    print("   python test/test_server.py")
    print("\n2. Abra o navegador e acesse:")
    print("   http://localhost:8000/test_form.html")
    print("\n3. Teste o bot:")
    print("   python main.py --dry-run")
    print("\n4. Execute o bot completo:")
    print("   python main.py")
    print("\n📖 Para mais informações, consulte:")
    print("   - README.md")
    print("   - TUTORIAL.md")
    print("\n⚠️  Lembre-se: Use apenas para fins educacionais!")
    print("=" * 60)

def main():
    """Main function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Falha na instalação das dependências")
        print("   Tente executar manualmente: pip install -r requirements.txt")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create sample data
    if not create_sample_data():
        print("\n⚠️  Aviso: Não foi possível criar dados de exemplo")
        print("   Você pode criar manualmente executando: python create_sample_data.py")
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main() 
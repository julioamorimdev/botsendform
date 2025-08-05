"""
Script to create sample Excel data for Form Bot testing
"""

import pandas as pd
import os
from pathlib import Path

def create_sample_data():
    """Create sample Excel file with test data"""
    
    # Sample data
    data = {
        'Nome': [
            'João Silva',
            'Maria Santos',
            'Pedro Oliveira',
            'Ana Costa',
            'Carlos Ferreira',
            'Lucia Rodrigues',
            'Roberto Almeida',
            'Fernanda Lima',
            'Marcos Pereira',
            'Juliana Souza'
        ],
        'Email': [
            'joao.silva@example.com',
            'maria.santos@example.com',
            'pedro.oliveira@example.com',
            'ana.costa@example.com',
            'carlos.ferreira@example.com',
            'lucia.rodrigues@example.com',
            'roberto.almeida@example.com',
            'fernanda.lima@example.com',
            'marcos.pereira@example.com',
            'juliana.souza@example.com'
        ],
        'Assunto': [
            'Consulta sobre produtos',
            'Solicitação de orçamento',
            'Dúvida sobre serviços',
            'Feedback sobre atendimento',
            'Proposta comercial',
            'Informações técnicas',
            'Reclamação',
            'Sugestão de melhoria',
            'Parceria comercial',
            'Agradecimento'
        ],
        'Mensagem': [
            'Gostaria de saber mais sobre os produtos disponíveis e seus preços.',
            'Preciso de um orçamento para 100 unidades do produto X.',
            'Tenho dúvidas sobre como funciona o serviço de suporte técnico.',
            'O atendimento foi excelente! Muito obrigado pela atenção.',
            'Gostaria de apresentar uma proposta comercial para sua empresa.',
            'Preciso de informações técnicas sobre a especificação do produto.',
            'Houve um problema com o último pedido realizado.',
            'Sugiro implementar um sistema de notificações por email.',
            'Interessado em estabelecer uma parceria comercial.',
            'Agradeço pelo excelente serviço prestado pela equipe.'
        ]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Create data directory if it doesn't exist
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    
    # Save to Excel
    excel_file = data_dir / 'sample_data.xlsx'
    df.to_excel(excel_file, index=False)
    
    print(f"Sample data created successfully: {excel_file}")
    print(f"Total rows: {len(df)}")
    print("\nSample data preview:")
    print(df.head(3).to_string(index=False))

if __name__ == "__main__":
    create_sample_data() 
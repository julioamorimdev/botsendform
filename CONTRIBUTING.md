# Contribuindo para o Form Bot

Obrigado por considerar contribuir para o Form Bot! Este documento fornece diretrizes e informações importantes para contribuidores.

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Configurando o Ambiente](#configurando-o-ambiente)
- [Diretrizes de Código](#diretrizes-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Reportando Bugs](#reportando-bugs)
- [Solicitando Funcionalidades](#solicitando-funcionalidades)
- [Código de Conduta](#código-de-conduta)
- [Licença](#licença)

## 🤝 Como Contribuir

Existem várias maneiras de contribuir para o projeto:

### 🐛 Reportando Bugs
- Use o template de issue para bugs
- Inclua informações detalhadas sobre o problema
- Adicione logs e screenshots quando relevante

### 💡 Sugerindo Melhorias
- Use o template de issue para funcionalidades
- Descreva claramente a funcionalidade desejada
- Explique o benefício para os usuários

### 🔧 Contribuindo com Código
- Fork o repositório
- Crie uma branch para sua feature
- Implemente suas mudanças
- Teste adequadamente
- Submeta um Pull Request

## 🛠️ Configurando o Ambiente

### Pré-requisitos
- Python 3.8+
- Git
- Editor de código (VS Code, PyCharm, etc.)

### Instalação Local

1. **Clone o repositório**
   ```bash
   git clone https://github.com/julioamorimdev/botsendform.git
   cd botsendform
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o ambiente**
   ```bash
   cp env.example .env
   # Edite o arquivo .env conforme necessário
   ```

5. **Execute os testes**
   ```bash
   python demo.py --dry-run
   ```

## 📝 Diretrizes de Código

### Estrutura do Projeto
Mantenha a estrutura modular existente:
```
botsendform/
├── main.py                 # Ponto de entrada principal
├── form_bot.py            # Lógica principal do bot
├── config.py              # Configurações
├── utils/                 # Utilitários
├── test/                  # Testes
├── data/                  # Dados de exemplo
└── docs/                  # Documentação
```

### Convenções de Código

#### Python
- Use **PEP 8** para estilo de código
- Docstrings em inglês para funções e classes
- Type hints quando possível
- Nomes descritivos para variáveis e funções

#### Exemplo de Código
```python
def process_form_data(data: pd.DataFrame) -> List[Dict]:
    """
    Process form data and return validated records.
    
    Args:
        data: DataFrame containing form data
        
    Returns:
        List of validated form records
        
    Raises:
        ValueError: If data is empty or invalid
    """
    if data.empty:
        raise ValueError("Data cannot be empty")
    
    validated_records = []
    for _, row in data.iterrows():
        if _validate_row(row):
            validated_records.append(row.to_dict())
    
    return validated_records
```

### Logging
- Use o sistema de logging existente
- Inclua logs informativos para debugging
- Evite logs sensíveis (senhas, dados pessoais)

### Tratamento de Erros
- Use exceções específicas
- Inclua mensagens de erro claras
- Implemente retry logic quando apropriado

## 🔄 Processo de Pull Request

### 1. Preparação
- Certifique-se de que sua branch está atualizada
- Execute todos os testes localmente
- Verifique se o código segue as diretrizes

### 2. Criação do PR
- Use um título descritivo
- Preencha o template de Pull Request
- Inclua screenshots se aplicável
- Referencie issues relacionadas

### 3. Template de Pull Request
```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Melhoria de documentação
- [ ] Refatoração

## Testes
- [ ] Testes unitários passaram
- [ ] Testes de integração passaram
- [ ] Testei manualmente

## Checklist
- [ ] Código segue as diretrizes de estilo
- [ ] Documentação foi atualizada
- [ ] Logs foram adicionados quando necessário
- [ ] Não há dados sensíveis expostos

## Screenshots (se aplicável)
```

### 4. Review Process
- Pelo menos um maintainer deve aprovar
- Todos os testes devem passar
- Código deve estar limpo e bem documentado

## 🐛 Reportando Bugs

### Template de Bug Report
```markdown
## Descrição do Bug
Descrição clara e concisa do bug

## Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## Comportamento Esperado
O que deveria acontecer

## Comportamento Atual
O que realmente acontece

## Screenshots
Se aplicável, adicione screenshots

## Ambiente
- OS: [ex: Windows 10]
- Python: [ex: 3.9.0]
- Versão do Bot: [ex: 1.0.0]

## Logs
Adicione logs relevantes aqui

## Informações Adicionais
Qualquer outra informação relevante
```

## 💡 Solicitando Funcionalidades

### Template de Feature Request
```markdown
## Descrição da Funcionalidade
Descrição clara da funcionalidade desejada

## Problema que Resolve
Explicação do problema que esta funcionalidade resolveria

## Solução Proposta
Descrição da solução proposta

## Alternativas Consideradas
Outras soluções que foram consideradas

## Contexto Adicional
Qualquer contexto adicional, screenshots, etc.
```

## 📋 Checklist de Contribuição

Antes de submeter sua contribuição, verifique:

### Para Bugs
- [ ] Bug é reproduzível
- [ ] Incluí logs relevantes
- [ ] Testei em diferentes ambientes
- [ ] Verifiquei se não é um problema conhecido

### Para Funcionalidades
- [ ] Funcionalidade é útil para a comunidade
- [ ] Implementei testes adequados
- [ ] Atualizei a documentação
- [ ] Não quebrei funcionalidades existentes

### Para Documentação
- [ ] Gramática e ortografia estão corretas
- [ ] Exemplos são claros e funcionais
- [ ] Links estão funcionando
- [ ] Formatação está consistente

## 🚀 Primeiros Passos

Se você é novo no projeto, aqui estão algumas issues boas para começar:

- Issues marcadas com `good first issue`
- Issues marcadas com `help wanted`
- Bugs simples ou melhorias de documentação

## 📞 Comunicação

- **Issues**: Para bugs e funcionalidades
- **Discussions**: Para perguntas e discussões gerais
- **Pull Requests**: Para contribuições de código

## 📜 Código de Conduta

### Nossos Padrões
- Seja respeitoso e inclusivo
- Use linguagem apropriada
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade

### Nossa Responsabilidade
- Manter um ambiente acolhedor
- Moderar comentários e commits
- Remover conteúdo inadequado
- Banir usuários que violam as regras

### Aplicação
- Reporte comportamento inadequado
- Maintainers investigarão e responderão
- Ações apropriadas serão tomadas

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [MIT License](LICENSE).

## 🙏 Agradecimentos

Obrigado por contribuir para o Form Bot! Suas contribuições ajudam a tornar esta ferramenta melhor para todos.

---

**Nota**: Este projeto é para fins educacionais. Certifique-se de que seu uso está em conformidade com as leis e termos de serviço aplicáveis. 
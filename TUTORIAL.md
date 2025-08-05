# Form Bot - Tutorial Completo

Este tutorial irá guiá-lo através do processo de configuração e uso do Form Bot para automatizar o preenchimento de formulários web.

## 📋 Índice

1. [Instalação](#instalação)
2. [Configuração Inicial](#configuração-inicial)
3. [Preparando os Dados](#preparando-os-dados)
4. [Testando o Sistema](#testando-o-sistema)
5. [Executando o Bot](#executando-o-bot)
6. [Configurações Avançadas](#configurações-avançadas)
7. [Solução de Problemas](#solução-de-problemas)

## 🛠️ Instalação

### 1. Pré-requisitos

Certifique-se de ter instalado:
- Python 3.7 ou superior
- Google Chrome browser

### 2. Instalar Dependências

```bash
# Navegue para o diretório do projeto
cd botsendform

# Instale as dependências
pip install -r requirements.txt
```

### 3. Verificar Instalação

```bash
# Teste se tudo está funcionando
python main.py --help
```

## ⚙️ Configuração Inicial

### 1. Configurar o Formulário

Edite o arquivo `config.py` para configurar o formulário que você deseja preencher:

```python
# URL do formulário
FORM_URL = "http://localhost:8000/test_form.html"

# Mapeamento dos campos do formulário (XPath)
FORM_FIELDS = {
    'name': '//*[@id="jform_contact_name"]',
    'email': '//*[@id="jform_contact_email"]',
    'subject': '//*[@id="jform_contact_emailmsg"]',
    'message': '//*[@id="jform_contact_message"]',
    'consent': '//*[@id="jform_consentbox0"]',
    'submit': '//*[@id="contact-form"]/div/div/button'
}
```

### 2. Configurar Arquivo Excel

```python
# Caminho para o arquivo Excel
EXCEL_FILE = "data/sample_data.xlsx"
```

## 📊 Preparando os Dados

### 1. Criar Dados de Exemplo

```bash
# Gere dados de exemplo
python create_sample_data.py
```

### 2. Estrutura do Excel

Seu arquivo Excel deve ter as seguintes colunas:

| Nome | Email | Assunto | Mensagem |
|------|-------|---------|----------|
| João Silva | joao@example.com | Consulta | Mensagem de teste |

### 3. Validar Dados

```bash
# Execute um teste seco para validar os dados
python main.py --dry-run
```

## 🧪 Testando o Sistema

### 1. Iniciar Servidor de Teste

```bash
# Inicie o servidor de teste
python test/test_server.py
```

### 2. Acessar Formulário de Teste

Abra seu navegador e acesse:
```
http://localhost:8000/test_form.html
```

### 3. Testar Manualmente

1. Preencha o formulário manualmente
2. Verifique se todos os campos estão funcionando
3. Teste o botão "Preencher Dados de Teste"

### 4. Testar com Dados Reais

```bash
# Teste com o formulário de teste
python main.py --excel data/sample_data.xlsx --url http://localhost:8000/test_form.html
```

## 🚀 Executando o Bot

### 1. Execução Básica

```bash
# Execute com configurações padrão
python main.py
```

### 2. Execução com Parâmetros

```bash
# Especificar arquivo Excel
python main.py --excel meu_arquivo.xlsx

# Especificar URL do formulário
python main.py --url https://meusite.com/contato

# Executar em modo headless (sem interface gráfica)
python main.py --headless

# Executar com logs detalhados
python main.py --verbose
```

### 3. Modo de Teste (Dry Run)

```bash
# Validar dados sem enviar formulários
python main.py --dry-run
```

## 🔧 Configurações Avançadas

### 1. Configurar Tempos de Espera

Edite `config.py`:

```python
TIMING = {
    'page_load_timeout': 30,        # Timeout para carregar página
    'element_wait_timeout': 10,     # Timeout para encontrar elementos
    'delay_between_submissions': 2,  # Delay entre envios
    'implicit_wait': 5              # Espera implícita
}
```

### 2. Configurar Browser

```python
BROWSER_CONFIG = {
    'headless': False,              # True para modo headless
    'window_size': (1920, 1080),    # Tamanho da janela
    'user_agent': 'Mozilla/5.0...'  # User agent personalizado
}
```

### 3. Configurar Logs

```python
LOGGING = {
    'level': 'INFO',                # Nível de log (DEBUG, INFO, WARNING, ERROR)
    'file': 'logs/form_bot.log',    # Arquivo de log
    'max_file_size': 10 * 1024 * 1024,  # Tamanho máximo do arquivo
    'backup_count': 5               # Número de backups
}
```

### 4. Configurar Tratamento de Erros

```python
ERROR_HANDLING = {
    'max_retries': 3,               # Máximo de tentativas
    'retry_delay': 5,               # Delay entre tentativas
    'continue_on_error': True       # Continuar em caso de erro
}
```

## 🎯 Exemplos de Uso

### Exemplo 1: Formulário de Contato Simples

```bash
# Configurar para formulário de contato
python main.py --excel contatos.xlsx --url https://empresa.com/contato
```

### Exemplo 2: Múltiplos Formulários

```bash
# Processar diferentes tipos de formulários
python main.py --excel leads.xlsx --url https://empresa.com/lead
python main.py --excel suporte.xlsx --url https://empresa.com/suporte
```

### Exemplo 3: Modo de Produção

```bash
# Executar em modo headless com logs detalhados
python main.py --headless --verbose --excel producao.xlsx
```

## 🔍 Solução de Problemas

### Problema: "ChromeDriver not found"

**Solução:**
```bash
# O webdriver-manager deve baixar automaticamente
# Se não funcionar, instale manualmente:
pip install webdriver-manager --upgrade
```

### Problema: "Element not found"

**Solução:**
1. Verifique os XPath no `config.py`
2. Use o modo `--verbose` para mais detalhes
3. Teste manualmente no navegador

### Problema: "Excel file not found"

**Solução:**
```bash
# Verifique o caminho do arquivo
python main.py --excel caminho/correto/arquivo.xlsx
```

### Problema: "Timeout waiting for element"

**Solução:**
1. Aumente os timeouts no `config.py`
2. Verifique a velocidade da internet
3. Use `--verbose` para debug

### Problema: "Form submission failed"

**Solução:**
1. Verifique se o formulário está funcionando manualmente
2. Confirme os IDs dos campos
3. Verifique se há captcha ou validação adicional

## 📝 Logs e Monitoramento

### Verificar Logs

```bash
# Logs são salvos em logs/form_bot.log
tail -f logs/form_bot.log
```

### Estatísticas de Execução

O bot exibe estatísticas ao final da execução:
- Total de linhas processadas
- Sucessos e falhas
- Taxa de sucesso
- Tempo de execução

## 🛡️ Boas Práticas

### 1. Sempre Teste Primeiro

```bash
# Sempre execute um dry-run primeiro
python main.py --dry-run --excel dados.xlsx
```

### 2. Use Modo Headless em Produção

```bash
# Para execuções em servidor
python main.py --headless --excel producao.xlsx
```

### 3. Monitore os Logs

```bash
# Acompanhe a execução
tail -f logs/form_bot.log
```

### 4. Valide Dados Antes

- Verifique se os emails são válidos
- Confirme que não há dados duplicados
- Teste com um pequeno conjunto primeiro

## 🚨 Avisos Importantes

⚠️ **Este projeto é para fins educacionais apenas**

- Não use para spam ou atividades maliciosas
- Respeite os termos de uso dos sites
- Não sobrecarregue servidores
- Use com responsabilidade

## 📞 Suporte

Se você encontrar problemas:

1. Verifique os logs em `logs/form_bot.log`
2. Execute com `--verbose` para mais detalhes
3. Teste manualmente o formulário
4. Verifique a configuração no `config.py`

---

**Lembre-se**: Use esta ferramenta de forma responsável e apenas para fins educacionais! 
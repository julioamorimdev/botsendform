# 🤖 Form Bot - Automated Form Submission Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://selenium-python.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributors](https://img.shields.io/github/contributors/julioamorimdev/botsendform)](https://github.com/julioamorimdev/botsendform/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/julioamorimdev/botsendform)](https://github.com/julioamorimdev/botsendform/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/julioamorimdev/botsendform)](https://github.com/julioamorimdev/botsendform/pulls)
[![Stars](https://img.shields.io/github/stars/julioamorimdev/botsendform)](https://github.com/julioamorimdev/botsendform/stargazers)

A powerful and flexible automated form submission tool that reads data from Excel spreadsheets and automatically fills and submits web forms using Selenium WebDriver. Perfect for educational purposes, testing, and learning web automation.

## ⚠️ Important Notice

**This project is intended for educational purposes only and should not be used for commercial purposes or to harm third parties. Users are responsible for ensuring their use complies with all applicable laws and terms of service.**

## 🌟 Features

- **📊 Excel Data Integration**: Read contact data from Excel spreadsheets with validation
- **🤖 Automated Form Filling**: Automatically fill web forms with data using Selenium
- **⚙️ Flexible Configuration**: Easy-to-configure form field mappings and templates
- **🛡️ Error Handling**: Robust error handling, retry mechanisms, and logging
- **🧪 Test Interface**: Built-in HTML test page and local server for development
- **🏗️ Modular Architecture**: Clean, maintainable code structure with separation of concerns
- **📝 Comprehensive Logging**: Colored console output and rotating file logs
- **🔧 CLI Interface**: Command-line interface with various options and dry-run mode
- **📱 Responsive Design**: Modern test form with responsive design
- **🌐 Multi-Platform**: Works on Windows, macOS, and Linux



## 📋 Prerequisites

- **Python 3.8+** (recommended: Python 3.9 or higher)
- **Google Chrome browser** (latest version recommended)
- **ChromeDriver** (automatically managed by webdriver-manager)
- **Git** (for cloning and version control)

## 🛠️ Installation

### Quick Start
```bash
# Clone the repository
git clone https://github.com/julioamorimdev/botsendform.git
cd botsendform

# Run the quick setup script
python quick_start.py
```

### Manual Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/julioamorimdev/botsendform.git
   cd botsendform
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp env.example .env
   # Edit .env file with your settings
   ```

5. **Generate sample data:**
   ```bash
   python create_sample_data.py
   ```

## 📖 Usage

### 🚀 Quick Demo
```bash
# Run a demo with test data
python demo.py

# Run in dry-run mode (no actual submissions)
python demo.py --dry-run
```

### Basic Usage

1. **Configure the form URL:**
   Edit `config.py` or set environment variables in `.env`:
   ```python
   FORM_URL = "https://your-form-url.com/contact"
   ```

2. **Prepare your Excel file:**
   Place your Excel file in the `data/` directory and update the filename in `config.py`:
   ```python
   EXCEL_FILE = "data/your_data.xlsx"
   ```

3. **Run the bot:**
   ```bash
   # Basic execution
   python main.py
   
   # With options
   python main.py --verbose --dry-run
   python main.py --excel-file data/my_data.xlsx
   ```

### Advanced Configuration

The bot supports custom field mappings and templates. Edit `config.py` to match your form's field IDs:

```python
FORM_FIELDS = {
    'name': '//*[@id="jform_contact_name"]',
    'email': '//*[@id="jform_contact_email"]',
    'subject': '//*[@id="jform_contact_emailmsg"]',
    'message': '//*[@id="jform_contact_message"]',
    'consent': '//*[@id="jform_consentbox0"]',
    'submit': '//*[@id="contact-form"]/div/div/button'
}
```

#### Using Form Templates
The project includes pre-configured templates for common platforms:

```python
from form_templates import get_template

# Use Joomla template
joomla_fields = get_template('joomla')

# Use WordPress template
wordpress_fields = get_template('wordpress')
```

## 🧪 Testing

### Using the Test HTML Page

1. **Start the test server:**
   ```bash
   python test/test_server.py
   # or
   cd test && python test_server.py
   ```

2. **Open your browser:**
   Navigate to `http://localhost:8000`

3. **Test the form:**
   Use the provided test form to verify your configuration

### Sample Data

The project includes a script to generate sample data:

```bash
python create_sample_data.py
```

This creates `data/sample_data.xlsx` with the following structure:

| Nome | Email | Assunto | Mensagem |
|------|-------|---------|----------|
| João Silva | joao@example.com | Test Subject | This is a test message |
| Maria Santos | maria@example.com | Another Test | Another test message |
| Pedro Costa | pedro@example.com | Third Test | Third test message |

## 📁 Project Structure

```
botsendform/
├── main.py                    # Main application entry point
├── form_bot.py               # Core bot functionality
├── config.py                 # Configuration settings
├── form_templates.py         # Pre-configured form templates
├── quick_start.py            # Quick setup script
├── demo.py                   # Demo script
├── create_sample_data.py     # Sample data generator
├── utils/
│   ├── __init__.py
│   ├── excel_reader.py       # Excel file processing
│   ├── form_handler.py       # Form interaction logic
│   └── logger.py             # Logging utilities
├── test/
│   ├── test_form.html        # Test form page
│   └── test_server.py        # Test server
├── data/
│   └── sample_data.xlsx      # Sample Excel file
├── logs/                     # Log files directory
├── .github/
│   ├── ISSUE_TEMPLATE/       # Issue templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── config.yml
├── requirements.txt          # Python dependencies
├── env.example              # Environment variables template
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # Contributing guidelines
├── CODE_OF_CONDUCT.md       # Code of conduct
├── TUTORIAL.md              # Detailed tutorial
├── FUTURE_IDEAS.md          # Future development ideas
└── README.md                # This file
```

## 🔧 Configuration

### Form Field Mapping

Customize form field selectors in `config.py`:

```python
FORM_FIELDS = {
    'name': 'input[name="full_name"]',
    'email': 'input[type="email"]',
    'subject': 'input[name="subject"]',
    'message': 'textarea[name="message"]',
    'consent': 'input[type="checkbox"]',
    'submit': 'button[type="submit"]'
}
```

### Timing Configuration

Adjust timing settings for different websites:

```python
TIMING = {
    'page_load_timeout': 30,
    'element_wait_timeout': 10,
    'delay_between_submissions': 2
}
```

## 📊 Logging

The bot provides detailed logging:

- **Console output**: Real-time progress updates
- **File logs**: Detailed logs saved to `logs/` directory
- **Error tracking**: Comprehensive error reporting

## 🚨 Error Handling

The bot includes robust error handling for:

- Network connectivity issues
- Form field not found
- Invalid Excel data
- Browser automation failures
- Rate limiting protection

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting your contribution.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** following our coding standards
4. **Add tests** if applicable
5. **Submit a pull request** using our template

### Types of Contributions

- 🐛 **Bug Reports**: Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- 💡 **Feature Requests**: Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- ❓ **Questions**: Use our [question template](.github/ISSUE_TEMPLATE/question.md)
- 📚 **Documentation**: Improve docs, tutorials, or examples
- 🔧 **Code**: Fix bugs, add features, or improve performance

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/botsendform.git
cd botsendform

# Set up development environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run tests
python demo.py --dry-run
```

### Code of Conduct

This project adheres to our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Important Notice**: This software is intended for EDUCATIONAL PURPOSES ONLY. Users are responsible for ensuring their use of this software complies with all applicable laws and terms of service of any websites or services they interact with.

## 👨‍💻 Author

**Júlio César de Amorim**

## 📞 Support & Community

- **📚 Documentation**: [TUTORIAL.md](TUTORIAL.md) - Detailed usage guide
- **🐛 Issues**: [GitHub Issues](https://github.com/julioamorimdev/botsendform/issues) - Report bugs or request features
- **💬 Discussions**: [GitHub Discussions](https://github.com/julioamorimdev/botsendform/discussions) - Ask questions and share ideas
- **📧 Email**: [Your Email] - Direct contact for urgent matters

## 🌟 Acknowledgments

- **Selenium WebDriver** - For web automation capabilities
- **Pandas** - For Excel data processing
- **Contributor Covenant** - For the Code of Conduct template
- **All Contributors** - For making this project better

## 📊 Project Status

- **Version**: 1.0.0
- **Status**: Active Development
- **Last Updated**: [Current Date]

## 🔮 Roadmap

See [FUTURE_IDEAS.md](FUTURE_IDEAS.md) for planned features and improvements.

---

**Remember**: Use this tool responsibly and only for educational purposes! 🎓
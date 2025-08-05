"""
Form Templates for Form Bot
Pre-configured templates for common form types
"""

# Template for Joomla Contact Form
JOOMLA_CONTACT_FORM = {
    'name': '//*[@id="jform_contact_name"]',
    'email': '//*[@id="jform_contact_email"]',
    'subject': '//*[@id="jform_contact_emailmsg"]',
    'message': '//*[@id="jform_contact_message"]',
    'consent': '//*[@id="jform_consentbox0"]',
    'submit': '//*[@id="contact-form"]/div/div/button'
}

# Template for WordPress Contact Form 7
WORDPRESS_CONTACT7_FORM = {
    'name': '//input[@name="your-name"]',
    'email': '//input[@name="your-email"]',
    'subject': '//input[@name="your-subject"]',
    'message': '//textarea[@name="your-message"]',
    'consent': '//input[@name="acceptance"]',
    'submit': '//input[@type="submit"]'
}

# Template for Bootstrap Contact Form
BOOTSTRAP_CONTACT_FORM = {
    'name': '//input[@name="name"]',
    'email': '//input[@type="email"]',
    'subject': '//input[@name="subject"]',
    'message': '//textarea[@name="message"]',
    'consent': '//input[@type="checkbox"]',
    'submit': '//button[@type="submit"]'
}

# Template for Simple HTML Contact Form
SIMPLE_HTML_FORM = {
    'name': '//input[@name="full_name"]',
    'email': '//input[@name="email"]',
    'subject': '//input[@name="subject"]',
    'message': '//textarea[@name="message"]',
    'consent': '//input[@name="agree"]',
    'submit': '//input[@type="submit"]'
}

# Template for Google Forms (basic structure)
GOOGLE_FORMS = {
    'name': '//input[@aria-label="Name"]',
    'email': '//input[@aria-label="Email"]',
    'subject': '//input[@aria-label="Subject"]',
    'message': '//textarea[@aria-label="Message"]',
    'consent': '//input[@type="checkbox"]',
    'submit': '//span[contains(text(), "Submit")]'
}

# Template for Wix Contact Form
WIX_CONTACT_FORM = {
    'name': '//input[@data-testid="input-field"]',
    'email': '//input[@type="email"]',
    'subject': '//input[@placeholder*="subject" or @placeholder*="assunto"]',
    'message': '//textarea[@data-testid="textarea-field"]',
    'consent': '//input[@type="checkbox"]',
    'submit': '//button[@data-testid="buttonElement"]'
}

# Template for Shopify Contact Form
SHOPIFY_CONTACT_FORM = {
    'name': '//input[@name="contact[name]"]',
    'email': '//input[@name="contact[email]"]',
    'subject': '//input[@name="contact[subject]"]',
    'message': '//textarea[@name="contact[body]"]',
    'consent': '//input[@name="contact[accepts_marketing]"]',
    'submit': '//input[@type="submit"]'
}

# Available templates
AVAILABLE_TEMPLATES = {
    'joomla': JOOMLA_CONTACT_FORM,
    'wordpress': WORDPRESS_CONTACT7_FORM,
    'bootstrap': BOOTSTRAP_CONTACT_FORM,
    'simple': SIMPLE_HTML_FORM,
    'google': GOOGLE_FORMS,
    'wix': WIX_CONTACT_FORM,
    'shopify': SHOPIFY_CONTACT_FORM
}

def get_template(template_name):
    """
    Get a form template by name
    
    Args:
        template_name: Name of the template
        
    Returns:
        Dictionary with form field mappings
        
    Raises:
        ValueError: If template not found
    """
    if template_name not in AVAILABLE_TEMPLATES:
        available = ', '.join(AVAILABLE_TEMPLATES.keys())
        raise ValueError(f"Template '{template_name}' not found. Available: {available}")
    
    return AVAILABLE_TEMPLATES[template_name]

def list_templates():
    """List all available templates"""
    print("Available form templates:")
    for name, template in AVAILABLE_TEMPLATES.items():
        print(f"  - {name}")
    return list(AVAILABLE_TEMPLATES.keys())

def print_template_info(template_name):
    """Print detailed information about a template"""
    if template_name not in AVAILABLE_TEMPLATES:
        print(f"Template '{template_name}' not found")
        return
    
    template = AVAILABLE_TEMPLATES[template_name]
    print(f"\nTemplate: {template_name.upper()}")
    print("=" * 40)
    for field, xpath in template.items():
        print(f"{field:10}: {xpath}")
    
    print("\nTo use this template, update your config.py:")
    print("FORM_FIELDS = form_templates.get_template('" + template_name + "')")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list":
            list_templates()
        else:
            print_template_info(sys.argv[1])
    else:
        print("Usage:")
        print("  python form_templates.py --list")
        print("  python form_templates.py <template_name>")
        print("\nExamples:")
        print("  python form_templates.py joomla")
        print("  python form_templates.py wordpress") 
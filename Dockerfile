# Dockerfile for Form Bot
# Multi-stage build for optimized production image

# Use Python 3.11 slim image as base
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Development stage
FROM base as development

# Install development dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional development tools
RUN pip install --no-cache-dir \
    pytest \
    pytest-cov \
    black \
    flake8 \
    isort \
    mypy \
    bandit \
    safety \
    pre-commit

# Copy source code
COPY . .

# Create necessary directories
RUN mkdir -p logs data

# Generate sample data
RUN python create_sample_data.py

# Expose port for test server
EXPOSE 8000

# Development command
CMD ["python", "demo.py", "--dry-run"]

# Production stage
FROM base as production

# Install only production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Create necessary directories
RUN mkdir -p logs data

# Generate sample data
RUN python create_sample_data.py

# Create non-root user for security
RUN groupadd -r formbot && useradd -r -g formbot formbot
RUN chown -R formbot:formbot /app
USER formbot

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Production command
CMD ["python", "main.py"]

# Test stage
FROM base as testing

# Install test dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install testing tools
RUN pip install --no-cache-dir \
    pytest \
    pytest-cov \
    pytest-mock \
    pytest-asyncio

# Copy source code
COPY . .

# Create necessary directories
RUN mkdir -p logs data

# Generate sample data
RUN python create_sample_data.py

# Run tests
CMD ["python", "-m", "pytest", "tests/", "-v", "--cov=utils", "--cov-report=html"]

# Documentation stage
FROM base as documentation

# Install documentation dependencies
RUN pip install --no-cache-dir \
    sphinx \
    sphinx-rtd-theme \
    myst-parser \
    sphinx-autodoc-typehints

# Copy source code
COPY . .

# Build documentation
RUN mkdir -p docs/_build
WORKDIR /app/docs
CMD ["make", "html"]

# Multi-stage build for final image
FROM production as final

# Add labels for better maintainability
LABEL maintainer="Júlio César de Amorim <seu-email@example.com>" \
      version="1.0.0" \
      description="Form Bot - Automated Form Submission Tool" \
      org.opencontainers.image.title="Form Bot" \
      org.opencontainers.image.description="A powerful and flexible automated form submission tool" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.authors="Júlio César de Amorim" \
      org.opencontainers.image.url="https://github.com/seu-usuario/botsendform" \
      org.opencontainers.image.source="https://github.com/seu-usuario/botsendform" \
      org.opencontainers.image.licenses="MIT"

# Add entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "main.py"] 
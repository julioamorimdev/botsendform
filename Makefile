# Makefile for Form Bot Project
# This file provides convenient commands for common development tasks

.PHONY: help install test lint format clean setup demo version release

# Default target
help:
	@echo "🤖 Form Bot - Development Commands"
	@echo ""
	@echo "📦 Setup & Installation:"
	@echo "  setup          - Set up the development environment"
	@echo "  install        - Install dependencies"
	@echo "  install-dev    - Install development dependencies"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  test           - Run tests"
	@echo "  lint           - Run linting checks"
	@echo "  format         - Format code with black and isort"
	@echo "  security       - Run security checks"
	@echo ""
	@echo "🚀 Development:"
	@echo "  demo           - Run demo script"
	@echo "  demo-dry       - Run demo in dry-run mode"
	@echo "  server         - Start test server"
	@echo "  sample-data    - Generate sample data"
	@echo ""
	@echo "📋 Version Management:"
	@echo "  version        - Show current version"
	@echo "  version-bump   - Bump patch version"
	@echo "  version-minor  - Bump minor version"
	@echo "  version-major  - Bump major version"
	@echo "  release        - Create a new release"
	@echo ""
	@echo "🧹 Maintenance:"
	@echo "  clean          - Clean up temporary files"
	@echo "  clean-all      - Clean everything including virtual environment"

# Setup and Installation
setup: install install-dev sample-data
	@echo "✅ Development environment setup complete!"

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

install-dev:
	@echo "🔧 Installing development dependencies..."
	pip install -e ".[dev,test,docs]"

# Testing and Quality
test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v

lint:
	@echo "🔍 Running linting checks..."
	flake8 .
	black --check .
	isort --check-only .
	mypy .

format:
	@echo "🎨 Formatting code..."
	black .
	isort .

security:
	@echo "🛡️ Running security checks..."
	bandit -r . -f json -o bandit-report.json || true
	safety check

# Development
demo:
	@echo "🚀 Running demo..."
	python demo.py

demo-dry:
	@echo "🚀 Running demo in dry-run mode..."
	python demo.py --dry-run

server:
	@echo "🌐 Starting test server..."
	python test/test_server.py

sample-data:
	@echo "📊 Generating sample data..."
	python create_sample_data.py

# Version Management
version:
	@echo "📋 Current version information:"
	python version.py show

version-bump:
	@echo "🔄 Bumping patch version..."
	python version.py bump patch

version-minor:
	@echo "🔄 Bumping minor version..."
	python version.py bump minor

version-major:
	@echo "🔄 Bumping major version..."
	python version.py bump major

release:
	@echo "🚀 Creating release..."
	@read -p "Enter release type (patch/minor/major): " release_type; \
	read -p "Enter release message: " release_message; \
	python version.py release $$release_type "$$release_message"

# Maintenance
clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.tmp" -delete
	find . -type f -name "*.temp" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -f .coverage
	rm -f coverage.xml

clean-all: clean
	@echo "🧹 Cleaning virtual environment..."
	rm -rf venv/
	rm -rf env/
	rm -rf .venv/

# Quick commands for common workflows
dev-setup: setup
	@echo "🎯 Development setup complete! You can now:"
	@echo "  - Run 'make demo' to test the bot"
	@echo "  - Run 'make server' to start the test server"
	@echo "  - Run 'make test' to run tests"

quick-test: format lint test
	@echo "✅ Quick test complete!"

pre-commit: format lint security test
	@echo "✅ Pre-commit checks passed!"

# Platform-specific commands
ifeq ($(OS),Windows_NT)
    PYTHON = python
    PIP = pip
    RM = del /Q
    RMDIR = rmdir /S /Q
else
    PYTHON = python3
    PIP = pip3
    RM = rm -f
    RMDIR = rm -rf
endif

# Docker commands (if needed in the future)
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t form-bot .

docker-run:
	@echo "🐳 Running Docker container..."
	docker run -it form-bot

# Documentation
docs-build:
	@echo "📚 Building documentation..."
	cd docs && make html

docs-serve:
	@echo "📚 Serving documentation..."
	cd docs/_build/html && python -m http.server 8001

# Backup and restore
backup:
	@echo "💾 Creating backup..."
	tar -czf backup-$(shell date +%Y%m%d-%H%M%S).tar.gz \
		--exclude='venv' \
		--exclude='__pycache__' \
		--exclude='*.pyc' \
		--exclude='.git' \
		--exclude='logs' \
		--exclude='data/*.xlsx' \
		.

# Show project status
status:
	@echo "📊 Project Status:"
	@echo "  Python version: $(shell $(PYTHON) --version)"
	@echo "  Current directory: $(PWD)"
	@echo "  Git status:"
	@git status --short || echo "  Not a git repository"
	@echo "  Dependencies:"
	@$(PIP) list | grep -E "(pandas|selenium|webdriver-manager)" || echo "  Dependencies not installed"

# Help for specific commands
help-setup:
	@echo "📦 Setup Commands:"
	@echo "  make setup      - Complete development environment setup"
	@echo "  make install    - Install production dependencies"
	@echo "  make install-dev - Install development dependencies"

help-test:
	@echo "🧪 Testing Commands:"
	@echo "  make test       - Run all tests"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code"
	@echo "  make security   - Run security checks"

help-dev:
	@echo "🚀 Development Commands:"
	@echo "  make demo       - Run demo script"
	@echo "  make server     - Start test server"
	@echo "  make sample-data - Generate sample data" 
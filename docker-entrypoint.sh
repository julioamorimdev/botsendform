#!/bin/bash
# Docker entrypoint script for Form Bot

set -e

# Function to print colored output
print_info() {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

print_success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

print_warning() {
    echo -e "\033[1;33m[WARNING]\033[0m $1"
}

print_error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
}

# Function to check if required environment variables are set
check_environment() {
    print_info "Checking environment variables..."
    
    # Check if FORM_URL is set
    if [ -z "$FORM_URL" ]; then
        print_warning "FORM_URL not set, using default: http://localhost:8000"
        export FORM_URL="http://localhost:8000"
    fi
    
    # Check if EXCEL_FILE is set
    if [ -z "$EXCEL_FILE" ]; then
        print_warning "EXCEL_FILE not set, using default: data/sample_data.xlsx"
        export EXCEL_FILE="data/sample_data.xlsx"
    fi
    
    print_success "Environment check completed"
}

# Function to wait for dependencies
wait_for_dependencies() {
    print_info "Checking dependencies..."
    
    # Check if Chrome is available
    if ! command -v google-chrome &> /dev/null; then
        print_error "Google Chrome is not installed or not in PATH"
        exit 1
    fi
    
    # Check if Python is available
    if ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH"
        exit 1
    fi
    
    print_success "Dependencies check completed"
}

# Function to create necessary directories
create_directories() {
    print_info "Creating necessary directories..."
    
    mkdir -p logs
    mkdir -p data
    mkdir -p screenshots
    
    print_success "Directories created"
}

# Function to generate sample data if needed
generate_sample_data() {
    if [ ! -f "data/sample_data.xlsx" ]; then
        print_info "Generating sample data..."
        python create_sample_data.py
        print_success "Sample data generated"
    else
        print_info "Sample data already exists"
    fi
}

# Function to run health check
health_check() {
    print_info "Running health check..."
    
    # Check if main application can be imported
    if python -c "import main; print('Main module imported successfully')" 2>/dev/null; then
        print_success "Health check passed"
        return 0
    else
        print_error "Health check failed"
        return 1
    fi
}

# Function to handle signals
handle_signal() {
    print_info "Received signal, shutting down gracefully..."
    exit 0
}

# Set up signal handlers
trap handle_signal SIGTERM SIGINT

# Main execution
main() {
    print_info "Starting Form Bot container..."
    
    # Check environment
    check_environment
    
    # Wait for dependencies
    wait_for_dependencies
    
    # Create directories
    create_directories
    
    # Generate sample data if needed
    generate_sample_data
    
    # Run health check
    if ! health_check; then
        print_error "Health check failed, exiting"
        exit 1
    fi
    
    print_success "Form Bot container started successfully"
    
    # Execute the main command
    exec "$@"
}

# Run main function with all arguments
main "$@" 
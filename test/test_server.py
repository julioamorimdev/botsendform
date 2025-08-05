"""
Test server for Form Bot
Provides a simple HTTP server to serve the test form
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

class FormBotTestServer:
    """Simple HTTP server for testing Form Bot"""
    
    def __init__(self, port=8000):
        self.port = port
        self.server = None
        
    def start(self):
        """Start the test server"""
        try:
            # Change to the test directory
            test_dir = Path(__file__).parent
            os.chdir(test_dir)
            
            # Create server
            handler = http.server.SimpleHTTPRequestHandler
            
            with socketserver.TCPServer(("", self.port), handler) as httpd:
                self.server = httpd
                print("=" * 60)
                print("FORM BOT TEST SERVER")
                print("=" * 60)
                print(f"Server running at: http://localhost:{self.port}")
                print(f"Test form available at: http://localhost:{self.port}/test_form.html")
                print("=" * 60)
                print("Press Ctrl+C to stop the server")
                print("=" * 60)
                
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\nServer stopped by user")
                    
        except OSError as e:
            if e.errno == 48:  # Address already in use
                print(f"Error: Port {self.port} is already in use.")
                print(f"Try using a different port: python test_server.py --port {self.port + 1}")
            else:
                print(f"Error starting server: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def stop(self):
        """Stop the test server"""
        if self.server:
            self.server.shutdown()

def main():
    """Main function with command-line argument parsing"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Form Bot Test Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_server.py              # Start server on port 8000
  python test_server.py --port 8080  # Start server on port 8080
        """
    )
    
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=8000,
        help='Port to run the server on (default: 8000)'
    )
    
    args = parser.parse_args()
    
    # Validate port
    if args.port < 1 or args.port > 65535:
        print("Error: Port must be between 1 and 65535")
        sys.exit(1)
    
    # Start server
    server = FormBotTestServer(args.port)
    server.start()

if __name__ == "__main__":
    main() 
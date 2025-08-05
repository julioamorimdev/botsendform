#!/usr/bin/env python3
"""
Version management script for Form Bot project.
This script helps manage version numbers and create version tags.
"""

import os
import sys
import subprocess
import re
from pathlib import Path

def read_version():
    """Read current version from VERSION file."""
    version_file = Path("VERSION")
    if version_file.exists():
        return version_file.read_text().strip()
    return "0.0.0"

def write_version(version):
    """Write version to VERSION file."""
    version_file = Path("VERSION")
    version_file.write_text(f"{version}\n")
    print(f"✅ Version updated to {version}")

def update_version_in_files(version):
    """Update version in various project files."""
    files_to_update = [
        ("README.md", r'Version.*?:\s*\*\*.*?\*\*', f'Version**: **{version}**'),
        ("README.md", r'Last Updated.*?:\s*\[.*?\]', f'Last Updated**: **[Current Date]**'),
    ]
    
    for file_path, pattern, replacement in files_to_update:
        if Path(file_path).exists():
            content = Path(file_path).read_text()
            updated_content = re.sub(pattern, replacement, content)
            Path(file_path).write_text(updated_content)
            print(f"✅ Updated version in {file_path}")

def validate_version(version):
    """Validate version format (semantic versioning)."""
    pattern = r'^\d+\.\d+\.\d+$'
    if not re.match(pattern, version):
        raise ValueError(f"Invalid version format: {version}. Use format: X.Y.Z")
    return True

def get_next_version(current_version, bump_type):
    """Calculate next version based on bump type."""
    major, minor, patch = map(int, current_version.split('.'))
    
    if bump_type == 'major':
        return f"{major + 1}.0.0"
    elif bump_type == 'minor':
        return f"{major}.{minor + 1}.0"
    elif bump_type == 'patch':
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid bump type: {bump_type}. Use: major, minor, or patch")

def create_git_tag(version, message=None):
    """Create a git tag for the version."""
    if message is None:
        message = f"Release version {version}"
    
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", f"Bump version to {version}"], check=True)
        
        # Create tag
        subprocess.run(["git", "tag", "-a", f"v{version}", "-m", message], check=True)
        
        print(f"✅ Git tag v{version} created successfully")
        print(f"📝 Tag message: {message}")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating git tag: {e}")
        return False
    
    return True

def push_changes(version):
    """Push changes and tags to remote repository."""
    try:
        # Push commits
        subprocess.run(["git", "push"], check=True)
        
        # Push tags
        subprocess.run(["git", "push", "--tags"], check=True)
        
        print(f"✅ Changes and tag v{version} pushed to remote repository")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error pushing changes: {e}")
        return False
    
    return True

def show_current_version():
    """Display current version information."""
    version = read_version()
    print(f"📋 Current version: {version}")
    
    # Check if there are uncommitted changes
    try:
        result = subprocess.run(["git", "status", "--porcelain"], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print("⚠️  There are uncommitted changes")
        else:
            print("✅ Working directory is clean")
    except subprocess.CalledProcessError:
        print("⚠️  Not a git repository or git not available")

def main():
    """Main function to handle version management."""
    if len(sys.argv) < 2:
        print("🤖 Form Bot Version Manager")
        print("\nUsage:")
        print("  python version.py show                    - Show current version")
        print("  python version.py bump <type>             - Bump version (major/minor/patch)")
        print("  python version.py set <version>           - Set specific version")
        print("  python version.py tag [message]           - Create git tag")
        print("  python version.py release <type> [message] - Bump version and create tag")
        print("\nExamples:")
        print("  python version.py show")
        print("  python version.py bump patch")
        print("  python version.py set 1.2.3")
        print("  python version.py tag 'Bug fixes and improvements'")
        print("  python version.py release minor 'New features added'")
        return
    
    command = sys.argv[1]
    
    try:
        if command == "show":
            show_current_version()
            
        elif command == "bump":
            if len(sys.argv) < 3:
                print("❌ Please specify bump type: major, minor, or patch")
                return
            
            bump_type = sys.argv[2]
            current_version = read_version()
            new_version = get_next_version(current_version, bump_type)
            
            print(f"🔄 Bumping version from {current_version} to {new_version}")
            write_version(new_version)
            update_version_in_files(new_version)
            
        elif command == "set":
            if len(sys.argv) < 3:
                print("❌ Please specify version number")
                return
            
            new_version = sys.argv[2]
            validate_version(new_version)
            
            print(f"🔄 Setting version to {new_version}")
            write_version(new_version)
            update_version_in_files(new_version)
            
        elif command == "tag":
            version = read_version()
            message = sys.argv[2] if len(sys.argv) > 2 else None
            
            print(f"🏷️  Creating git tag for version {version}")
            if create_git_tag(version, message):
                print("✅ Tag created successfully")
            
        elif command == "release":
            if len(sys.argv) < 3:
                print("❌ Please specify release type: major, minor, or patch")
                return
            
            bump_type = sys.argv[2]
            message = sys.argv[3] if len(sys.argv) > 3 else None
            
            current_version = read_version()
            new_version = get_next_version(current_version, bump_type)
            
            print(f"🚀 Creating release {new_version}")
            
            # Bump version
            write_version(new_version)
            update_version_in_files(new_version)
            
            # Create tag
            if create_git_tag(new_version, message):
                # Push changes
                push_changes(new_version)
                print(f"🎉 Release {new_version} created and pushed successfully!")
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Use 'python version.py' to see available commands")
            
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 
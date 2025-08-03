#!/usr/bin/env python3

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def check_requirements():
    try:
        import pandas
        import openpyxl
        return True
    except ImportError:
        return False

def install_requirements():
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def create_excel_if_needed():
    if not os.path.exists('data.xlsx'):
        print("Creating Excel template...")
        subprocess.check_call([sys.executable, "create_excel_template.py"])
        print("\nExcel template created. Please edit 'data.xlsx' with your blog content.")
        return False
    return True

def generate_blog():
    print("Generating blog...")
    subprocess.check_call([sys.executable, "generate_blog.py"])

def open_browser():
    if os.path.exists('index.html'):
        print("Opening blog in web browser...")
        webbrowser.open('file://' + str(Path('index.html').absolute()))

def main():
    print("\n===== UNSUNG INDIA by Ikshana Blog Generator =====\n")
    
    # Check and install requirements if needed
    if not check_requirements():
        print("Required packages not found.")
        install_requirements()
    
    # Create Excel template if needed
    excel_exists = create_excel_if_needed()
    
    if excel_exists:
        # Generate blog
        generate_blog()
        
        # Open in browser
        open_browser()
    else:
        print("\nAfter editing the Excel file, run this script again to generate your blog.")
    
    print("\n===== Done =====\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
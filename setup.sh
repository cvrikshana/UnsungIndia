#!/bin/bash

echo "Setting up UNSUNG INDIA by Ikshana Blog Generator..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Install required packages
echo "Installing required Python packages..."
pip3 install pandas openpyxl

# Create Excel template
echo "Creating Excel template..."
python3 create_excel_template.py

echo ""
echo "Setup complete! Here's what to do next:"
echo "1. Edit 'data.xlsx' with your blog content"
echo "2. Add your images to the 'images' folder"
echo "3. Run 'python3 generate_blog.py' to generate your blog"
echo "4. Open 'index.html' in a web browser to view your blog"
echo ""
echo "Enjoy your UNSUNG INDIA blog!"
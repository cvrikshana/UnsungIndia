@echo off
echo Setting up UNSUNG INDIA by Ikshana Blog Generator...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH. Please install Python and try again.
    pause
    exit /b 1
)

:: Install required packages
echo Installing required Python packages...
pip install pandas openpyxl

:: Create Excel template
echo Creating Excel template...
python create_excel_template.py

echo.
echo Setup complete! Here's what to do next:
echo 1. Edit 'data.xlsx' with your blog content
echo 2. Add your images to the 'images' folder
echo 3. Run 'python generate_blog.py' to generate your blog
echo 4. Open 'index.html' in a web browser to view your blog
echo.
echo Enjoy your UNSUNG INDIA blog!

pause
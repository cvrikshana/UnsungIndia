import os
import webbrowser
import platform

def preview_blog():
    # Get the absolute path to index.html
    index_path = os.path.abspath('index.html')
    
    # Check if index.html exists
    if not os.path.exists(index_path):
        print("Error: index.html not found. Please run generate_blog.py first.")
        return
    
    # Convert the file path to a URL
    if platform.system() == 'Windows':
        url = 'file:///' + index_path.replace('\\', '/')
    else:
        url = 'file://' + index_path
    
    # Open the URL in the default web browser
    print(f"Opening {url} in your default web browser...")
    webbrowser.open(url)

if __name__ == "__main__":
    preview_blog()
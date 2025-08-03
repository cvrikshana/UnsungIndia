#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil

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

def check_vercel_cli():
    try:
        subprocess.check_call(["vercel", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def install_vercel_cli():
    print("Vercel CLI not found. Installing...")
    try:
        subprocess.check_call(["npm", "install", "-g", "vercel"])
        print("Vercel CLI installed successfully.")
        return True
    except subprocess.SubprocessError:
        print("Error installing Vercel CLI. Please install it manually with 'npm install -g vercel'")
        return False

def generate_blog():
    print("Generating blog...")
    # Import here to avoid issues if pandas is not installed
    from generate_blog import generate_html
    generate_html()

def prepare_for_vercel():
    print("Preparing files for Vercel deployment...")
    
    # Create a deployment directory
    deploy_dir = "vercel_deploy"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy necessary files
    if os.path.exists("index.html"):
        shutil.copy("index.html", os.path.join(deploy_dir, "index.html"))
    else:
        print("Error: index.html not found. Run the script again after creating data.xlsx")
        return False
    
    # Copy static files
    for file in ["styles.css", "vercel.json", "manifest.json"]:
        if os.path.exists(file):
            shutil.copy(file, os.path.join(deploy_dir, file))
    
    # Create images directory and copy images
    if os.path.exists("images"):
        images_dir = os.path.join(deploy_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        for file in os.listdir("images"):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
                shutil.copy(os.path.join("images", file), os.path.join(images_dir, file))
    
    return True

def deploy_to_vercel():
    print("\nDeploying to Vercel...")
    os.chdir("vercel_deploy")
    
    try:
        # Run vercel command to deploy
        subprocess.check_call(["vercel", "--prod"])
        print("\nDeployment successful! Your blog is now live on Vercel.")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error deploying to Vercel: {str(e)}")
        print("You can try deploying manually by running 'vercel --prod' in the vercel_deploy directory")
        return False

def main():
    print("\n===== UNSUNG INDIA by Ikshana - Vercel Deployment =====\n")
    
    # Check and install Python requirements if needed
    if not check_requirements():
        print("Required Python packages not found.")
        install_requirements()
    
    # Check if data.xlsx exists
    if not os.path.exists('data.xlsx'):
        print("Error: data.xlsx not found. Please create an Excel file with columns: ImagePath, Title, Description")
        print("You can run 'python create_excel_template.py' to create a template.")
        return
    
    # Generate blog
    generate_blog()
    
    # Check and install Vercel CLI if needed
    if not check_vercel_cli():
        if not install_vercel_cli():
            return
    
    # Prepare files for Vercel
    if not prepare_for_vercel():
        return
    
    # Deploy to Vercel
    deploy_to_vercel()
    
    print("\n===== Done =====\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
import pandas as pd
import os
from datetime import datetime

def generate_html():
    # Check if data.xlsx exists
    if not os.path.exists('data.xlsx'):
        print("Error: data.xlsx not found. Please create an Excel file with columns: ImagePath, Title, Description")
        return
    
    try:
        # Read the Excel file
        df = pd.read_excel('data.xlsx')
        
        # Check if required columns exist
        required_columns = ['ImagePath', 'Title', 'Description']
        for col in required_columns:
            if col not in df.columns:
                print(f"Error: Column '{col}' not found in data.xlsx")
                return
        
        # Create images directory if it doesn't exist
        if not os.path.exists('images'):
            os.makedirs('images')
            print("Created 'images' directory. Please place your images there.")
        
        # Generate HTML content
        html_content = generate_html_content(df)
        
        # Write to index.html
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("Successfully generated index.html")
        print("To view your blog, open index.html in a web browser")
        
    except Exception as e:
        print(f"Error generating blog: {str(e)}")

def generate_html_content(df):
    # HTML template
    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="UNSUNG INDIA by Ikshana - Stories of unsung heroes and hidden treasures of India">
    <meta name="theme-color" content="#ffffff">
    <title>UNSUNG INDIA by Ikshana</title>
    <link rel="manifest" href="manifest.json">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Source+Sans+Pro:wght@300;400;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="logo" onclick="returnToMainPage()">
            <img src="Unsung-2.png" alt="Unsung India Logo">
        </div>
    </header>
    
    <main>
'''
    
    # Generate blog posts
    for _, row in df.iterrows():
        image_path = row['ImagePath']
        title = row['Title']
        description = row['Description']
        
        html += f'''
        <article class="post" onclick="openFullPost('{image_path}', '{title}', '{description}')">
            <div class="post-image">
                <img src="{image_path}" alt="{title}">
            </div>
            <div class="post-content">
                <h2>{title}</h2>
                <p>{description}</p>
            </div>
        </article>
'''
    
    # Close HTML
    html += f'''
    </main>
    
    <div id="fullPostView" class="full-post-view">
        <div class="full-post-content">
            <div class="back-button" onclick="closeFullPost()">← Back</div>
            <img id="fullPostImage" class="full-post-image" src="" alt="">
            <h2 id="fullPostTitle" class="full-post-title"></h2>
            <p id="fullPostDescription" class="full-post-description"></p>
        </div>
    </div>
    
    <footer>
        <p>&copy; {datetime.now().year} UNSUNG INDIA by Ikshana. All rights reserved.</p>
    </footer>
    
    <script>
        function openFullPost(imagePath, title, description) {{
            document.getElementById('fullPostImage').src = imagePath;
            document.getElementById('fullPostImage').alt = title;
            document.getElementById('fullPostTitle').textContent = title;
            document.getElementById('fullPostDescription').textContent = description;
            document.getElementById('fullPostView').style.display = 'block';
            document.body.style.overflow = 'hidden';
            window.scrollTo(0, 0);
        }}
        
        function closeFullPost() {{
            document.getElementById('fullPostView').style.display = 'none';
            document.body.style.overflow = 'auto';
        }}
        
        function returnToMainPage() {{
            // If in full post view, close it and return to main page
            if (document.getElementById('fullPostView').style.display === 'block') {{
                closeFullPost();
            }}
            // If already on main page, scroll to top
            else {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }}
        }}
        
        // Close full post view with escape key
        document.addEventListener('keydown', function(event) {{
            if (event.key === 'Escape') {{
                closeFullPost();
            }}
        }});
    </script>
</body>
</html>
'''
    
    return html

if __name__ == "__main__":
    generate_html()
    print("\nPlease ensure you have the following:")
    print("1. data.xlsx file with columns: ImagePath, Title, Description")
    print("2. Images placed in the 'images' directory (or as specified in ImagePath column)")
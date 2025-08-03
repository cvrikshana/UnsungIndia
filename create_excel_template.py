import pandas as pd
import os

def create_excel_template():
    # Check if data.xlsx already exists
    if os.path.exists('data.xlsx'):
        overwrite = input("data.xlsx already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation cancelled.")
            return
    
    # Sample data
    data = {
        'ImagePath': [
            'images/3.jpeg',
            'images/3.jpeg',
            'images/3.jpeg'
        ],
        'Title': [
            'The Forgotten Artisans of Kutch',
            'Living Bridges of Meghalaya',
            'The Last Manuscript Keepers'
        ],
        'Description': [
            'Exploring the intricate handicrafts and the stories of artisans preserving centuries-old traditions in the remote villages of Kutch, Gujarat.',
            'Discover the incredible living root bridges of Meghalaya, hand-shaped by the Khasi and Jaintia tribes over decades using the roots of rubber fig trees.',
            'Meet the families in Varanasi who have been safeguarding ancient Sanskrit manuscripts for generations, preserving knowledge that dates back thousands of years.'
        ]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel('data.xlsx', index=False)
    
    print("Excel template created successfully: data.xlsx")
    print("You can now edit this file with your own blog content.")
    
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
        print("Created 'images' directory. Please place your images there.")

if __name__ == "__main__":
    try:
        create_excel_template()
    except Exception as e:
        print(f"Error creating Excel template: {str(e)}")
        print("Make sure you have pandas and openpyxl installed:")
        print("pip install pandas openpyxl")
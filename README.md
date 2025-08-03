# UNSUNG INDIA by Ikshana - Blog Generator

A minimalist blog website generator that creates a clean, responsive blog from Excel data. Optimized for Vercel deployment and fully responsive across all screen resolutions.

## Features

- Clean, single-column vertical layout
- Modern, monochromatic, typography-focused design
- Fully responsive for all devices (mobile, tablet, desktop, and large screens)
- Dynamic content generation from Excel data
- Progressive Web App (PWA) capabilities
- Optimized for Vercel deployment
- Simple to set up and deploy

## Requirements

- Python 3.6 or higher
- pandas library (`pip install pandas`)
- openpyxl library (`pip install openpyxl`)

## Setup Instructions

1. Install required Python packages:
   ```
   pip install pandas openpyxl
   ```

2. Create an Excel file named `data.xlsx` with the following columns:
   - `ImagePath`: Path to the image file (e.g., "images/photo1.jpg")
   - `Title`: Title of the blog post
   - `Description`: Content/description of the blog post

3. Create an `images` folder and place all your images there (or as specified in the ImagePath column)

4. Run the generator script:
   ```
   python generate_blog.py
   ```

5. Open the generated `index.html` file in a web browser to view your blog

## File Structure

```
/
├── generate_blog.py    # Python script to generate the blog
├── data.xlsx          # Excel file containing blog content
├── styles.css         # CSS styling for the blog
├── index.html         # Generated HTML file (created by the script)
├── images/            # Folder containing all blog images
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── README.md          # This file
```

## Customization

You can customize the appearance of your blog by modifying the `styles.css` file. The current design features:

- Playfair Display font for headings
- Source Sans Pro font for body text
- Subtle hover effects on blog posts
- Responsive design for all screen sizes

## Deployment

### Vercel Deployment (Recommended)

This project is optimized for Vercel deployment. To deploy to Vercel:

1. Make sure you have generated your blog by running `python generate_blog.py`
2. Use the included deployment script:
   ```
   python deploy_to_vercel.py
   ```
   This script will:
   - Generate your blog if needed
   - Install Vercel CLI if not already installed
   - Prepare your files for deployment
   - Deploy your site to Vercel

3. Follow the prompts from the Vercel CLI to complete the deployment
4. Your site will be live at a URL provided by Vercel (e.g., `unsung-india.vercel.app`)

### Manual Deployment

The generated blog is a static website that can be deployed to any web hosting service:

1. Upload all files (index.html, styles.css, manifest.json, and the images folder) to your web hosting service
2. No server-side processing is required as this is a static website

## License

This project is open-source and available for personal and commercial use.
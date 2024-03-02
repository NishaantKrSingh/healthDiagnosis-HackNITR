# main.py
import os
from dotenv import load_dotenv
from google_generativeai import GeminiClient

# Load environment variables
load_dotenv()

def describe_image(image_path):
    try:
        # Describe content using Google API
        prompt = "Can you explain this in simple words."
        response = GeminiClient.generate_content(prompt, image_path=image_path)

        # Extract the description
        description = response.text
        return description
    except Exception as e:
        return f"Error: {str(e)}"

def upload_image():
    try:
        # Replace this with your file dialog logic to get the image path interactively
        image_path = "path/to/your/image.jpg"  

        # Call the describe_image function
        description = describe_image(image_path)

        # Print the description
        print(f"Image description: {description}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    upload_image()

if __name__ == "__main__":
    main()

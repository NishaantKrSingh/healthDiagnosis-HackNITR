# main.py
import os
from dotenv import load_dotenv
from google_generativeai import GeminiClient

# Load environment variables
load_dotenv()

def describe_image(image_path):
    """
    Describes the content of an image using the Google Gemini API.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Description of the image content.
    """
    try:
        # Describe content using Google API
        prompt = "What is in the image?"
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

if __name__ == "__main__":
    upload_image()

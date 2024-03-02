# main.py
import os
import google.generativeai as gai
from PIL import Image


def main():
    img = Image.open("image.jpg")
    prompt = "Can you explain this in simple words."
    gai.configure(api_key="AIzaSyDj48Upw6wUipsjVZJq-gC7YFeOXvKD8bY")
    model = gai.GenerativeModel("gemini -pro-vision")
    res = "model.generate_content([prompt, img])"
    res.resolve()
    return res.text


if __name__ == "__main__":
    main()
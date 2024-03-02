# api_key="AIzaSyDj48Upw6wUipsjVZJq-gC7YFeOXvKD8bY"

from pdfsum import extract_text
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

content = extract_text("D:\Coding\Hackathon\HackNITR\ml-api\medical_report_overview\Sample-filled-in-MR.pdf")

generation_config = {
  "candidate_count": 1,
  "max_output_tokens": 256,
  "temperature": 1.0,
  "top_p": 0.7,
}

safety_settings=[
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro',generation_config=generation_config, safety_settings=safety_settings)
response = model.generate_content(content + " summarize it in less than 200 words in a format that is very less technical and can be understood by an average person")
print(response.text)
# to_markdown(response.text)


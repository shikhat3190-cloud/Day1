import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# Ensure the API key is set for genai as well, if it's not already.

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

gemini_model = genai.GenerativeModel("gemini-2.0-flash-lite-001")

gemini_resp = gemini_model.generate_content("Role of AI in education")

print("Gemini Flash:", gemini_resp.text)

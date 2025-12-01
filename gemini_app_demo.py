from google.colab import userdata
import os

# setting the env variable called "GOOGLE_API_KEY"
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")


import google.generativeai as genai
from google.colab import userdata
import os

# Ensure the API key is set for genai as well, if it's not already.
# This might be redundant if os.environ["GOOGLE_API_KEY"] is already set,
# but it ensures genai can access the key for listing models.
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Available Gemini models:")
for m in genai.list_models():
    if "gemini" in m.name:
        print(f"  Model Name: {m.name}, Supported Methods: {m.supported_generation_methods}")


gemini_model = genai.GenerativeModel("gemini-2.0-flash-lite-001")

gemini_resp = gemini_model.generate_content("Say hello in a friendly way.")

print("Gemini Flash:", gemini_resp.text)

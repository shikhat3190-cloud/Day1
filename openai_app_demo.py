import os
from google.colab import userdata

# Ensure your OpenAI API key is set as an environment variable
# You can set it in Colab's secrets manager (named OPENAI_API_KEY)
# or directly: os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")


from openai import OpenAI
openai_client = OpenAI()
gpt_resp = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hello in a friendly way."}
    ]
)

print("GPT-4o-mini:", gpt_resp.choices[0].message.content)

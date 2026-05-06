from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"user","content":"Hey There"}
    ]
)

print(response.choices[0].message.content)
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create Model
model = genai.GenerativeModel("gemini-2.5-flash")

print("=" * 50)
print("🤖 AI Business Assistant")
print("=" * 50)

while True:
    prompt = input("\nYou: ")

    if prompt.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        response = model.generate_content(prompt)
        print("\n🤖 AI:")
        print(response.text)

    except Exception as e:
        print("\nError:", e)
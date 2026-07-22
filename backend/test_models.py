from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print("=" * 80)
    print("Name:", model.name)

    if hasattr(model, "display_name"):
        print("Display:", model.display_name)

    if hasattr(model, "supported_actions"):
        print("Supported Actions:", model.supported_actions)
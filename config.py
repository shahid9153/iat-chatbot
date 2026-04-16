import google.genai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please create a .env file with your API key.")

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("Client configured successfully at import")
except Exception as e:
    print(f"Failed to configure client at import: {e}")
    client = None

def configure():
    # Keep for compatibility, but client is already created
    pass




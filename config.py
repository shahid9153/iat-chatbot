import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyD1ro9D2TeWPI-I_WqoWgZSlKIs-_bGnMs"

def configure():
    genai.configure(api_key=GEMINI_API_KEY)




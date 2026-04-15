import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyD1ro9D2TeWPI-I_WqoWgZaaaaa-_aaaaa"

def configure():
    genai.configure(api_key=GEMINI_API_KEY)




import google.generativeai as genai
import csv
import os
from prompt import SYSTEM_PROMPT, KNOWLEDGE_BASE

model = genai.GenerativeModel("gemini-2.5-flash")

# 📊 Save leads
def save_lead(name, email, message):
    file_exists = os.path.isfile("leads.csv")

    with open("leads.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Email", "Message"])

        writer.writerow([name, email, message])


def get_response(user_input):
    try:
        full_prompt = SYSTEM_PROMPT + "\n" + KNOWLEDGE_BASE + "\nUser: " + user_input
        response = model.generate_content(full_prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "Sorry, I couldn't understand that."

    except Exception:
        return "⚠️ Server busy. Please try again later."
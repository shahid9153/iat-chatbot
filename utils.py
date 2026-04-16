import google.genai as genai
import csv
import os
from prompt import SYSTEM_PROMPT, KNOWLEDGE_BASE
from config import client

# 📊 Save leads
def save_lead(name, email, message):
    file_exists = os.path.isfile("leads.csv")

    with open("leads.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Email", "Message"])

        writer.writerow([name, email, message])


def get_response(user_input, chat_history=None):
    if not client:
        return "⚠️ Chatbot is not configured properly. Please check the API key."

    try:
        # Build conversation context
        context = SYSTEM_PROMPT + "\n" + KNOWLEDGE_BASE + "\n\nConversation History:\n"
        if chat_history:
            for role, msg in chat_history[-10:]:  # Last 10 messages for context
                context += f"{role.capitalize()}: {msg}\n"
        context += f"User: {user_input}\nAssistant:"

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=context
        )

        if response and hasattr(response, "text"):
            return response.text.strip()

        return "Sorry, I couldn't generate a response."

    except genai.errors.ClientError as e:
        if "403" in str(e) or "PERMISSION_DENIED" in str(e):
            return "⚠️ Invalid API key. Please check your configuration."
        elif "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            return "⚠️ Rate limit exceeded. Please try again later."
        else:
            return f"⚠️ API error: {str(e)}"
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"
# IAT Networks Chatbot

A professional chatbot for IAT Networks built with Streamlit and Google Gemini AI.

## Setup

1. **Clone the repository and install dependencies:**
   ```bash
   git clone <repository-url>
   cd iat-chatbot
   pip install -r requirements.txt
   ```

2. **Set up your API key securely:**
   - Create a `.env` file in the project root:
     ```bash
     touch .env
     ```
   - Add your Google Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your-api-key-here
     ```
   - The `.env` file is automatically ignored by git for security

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Security Notes

- Never commit API keys to version control
- The `.env` file is gitignored for your safety
- API keys are loaded securely using python-dotenv

## Features

- Conversational AI assistant for IT, BPO, and recruitment services
- Lead capture form for interested users
- Clean, modern UI
- Conversation history awareness

## Configuration

- The chatbot uses Gemini 2.0 Flash model
- Prompts are defined in `prompt.py`
- API configuration in `config.py`
- Utility functions in `utils.py`

## Deployment

This app can be deployed on Streamlit Cloud, Heroku, or any platform supporting Streamlit apps. Make sure to set the `GEMINI_API_KEY` environment variable in your deployment environment.
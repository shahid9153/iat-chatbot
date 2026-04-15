import streamlit as st
import time
from config import configure
from utils import get_response, save_lead

# 🔑 Configure API
configure()

st.set_page_config(page_title="IAT Chatbot", layout="centered")

# 🎨 CLEAN UI (LIGHT MODE FIXED)
st.markdown("""
<style>

/* Force light theme */
html, body, [class*="css"] {
    background-color: #eef2f7 !important;
    color: #111 !important;
}

/* Remove extra spacing */
.block-container {
    padding-top: 1rem !important;
}

/* Hide default UI */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Chat container */
.chat-container {
    width: 380px;
    margin: 30px auto;
    background: white;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    overflow: hidden;
}

/* Header */
.chat-header {
    background: #2563eb;
    color: white;
    padding: 14px;
    text-align: center;
    font-weight: 600;
}

/* Chat body */
.chat-body {
    height: 420px;
    overflow-y: auto;
    padding: 12px;
    background: #f8fafc;
}

/* Messages */
.msg {
    padding: 10px 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    max-width: 75%;
    font-size: 14px;
    animation: fadeIn 0.3s ease-in-out;
}

.bot {
    background: #e5e7eb;
    color: #111;
}

.user {
    background: #2563eb;
    color: white;
    margin-left: auto;
}

/* Typing animation */
.typing {
    display: flex;
    gap: 4px;
}

.dot {
    width: 6px;
    height: 6px;
    background: #666;
    border-radius: 50%;
    animation: blink 1.4s infinite both;
}

.dot:nth-child(2) { animation-delay: 0.2s; }
.dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes blink {
    0% { opacity: 0.2; }
    20% { opacity: 1; }
    100% { opacity: 0.2; }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Input */
.stForm {
    border-top: 1px solid #ddd;
    padding: 10px;
    background: white;
}

input[type="text"] {
    background: white !important;
    color: #111 !important;
    border: 1px solid #ccc !important;
    border-radius: 8px !important;
    padding: 10px !important;
}

button {
    background: #2563eb !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
}

/* Lead form */
.lead-box {
    width: 380px;
    margin: 15px auto;
    padding: 15px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# 🧠 Session State
if "chat" not in st.session_state:
    st.session_state.chat = [
        ("bot", "👋 Hello! I'm the IAT Networks assistant. How can I help you today?")
    ]

if "typing" not in st.session_state:
    st.session_state.typing = False

if "show_form" not in st.session_state:
    st.session_state.show_form = False

# 💬 Chat UI
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown('<div class="chat-header">IAT Networks Support</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-body">', unsafe_allow_html=True)

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="msg user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="msg bot">{msg}</div>', unsafe_allow_html=True)

# Typing animation
if st.session_state.typing:
    st.markdown("""
    <div class="msg bot">
        <div class="typing">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 📝 Input
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([4,1])
    user_input = col1.text_input("Type your message...", label_visibility="collapsed")
    send = col2.form_submit_button("Send")

# 🚀 Handle user input
if send and user_input:
    st.session_state.chat.append(("user", user_input))
    st.session_state.typing = True
    st.rerun()

# 🤖 Generate response
if st.session_state.typing:
    time.sleep(1)

    user_msg = st.session_state.chat[-1][1]
    bot_reply = get_response(user_msg)

    # 🎯 Trigger lead form
    if any(word in user_msg.lower() for word in ["interested", "price", "cost", "service", "hire", "job"]):
        st.session_state.show_form = True
        bot_reply += "\n\n👉 Please share your details below."

    st.session_state.chat.append(("bot", bot_reply))
    st.session_state.typing = False
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# 📞 Lead Capture Form
if st.session_state.show_form:
    st.markdown('<div class="lead-box">', unsafe_allow_html=True)
    st.markdown("### 📞 Get in Touch")

    with st.form("lead_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Requirement")

        submit = st.form_submit_button("Submit")

        if submit:
            save_lead(name, email, message)
            st.success("✅ Our team will contact you soon!")
            st.session_state.show_form = False

    st.markdown('</div>', unsafe_allow_html=True)
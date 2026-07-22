import streamlit as st
from utils.gemini_chat import multilingual_chat

st.set_page_config(
    page_title="🌍 Multilingual AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.title("🌍 Multilingual AI")
    st.markdown("---")
    st.write("### Supported Languages")
    st.write("🇬🇧 English")
    st.write("🇮🇳 Hindi")
    st.write("🇫🇷 French")
    st.write("🇪🇸 Spanish")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------- Title ---------------- #

st.title("🤖 Multilingual AI Chatbot")

st.caption("Automatic Language Detection | Gemini AI")

# ---------- Chat History ---------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------- User Input -------- #

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response, language = multilingual_chat(prompt)

        language_names = {
            "en": "English",
            "hi": "Hindi",
            "fr": "French",
            "es": "Spanish"
        }

        st.success(
            f"🌐 Language: {language_names.get(language, language)}"
        )

        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
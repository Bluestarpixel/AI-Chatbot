from utils.gemini_chat import (
    chat_with_gemini,
    analyze_image,
    generate_image
)
import streamlit as st
from PIL import Image
from utils.gemini_chat import chat_with_gemini, analyze_image

st.set_page_config(
    page_title="Multi-Modal Chatbot",
    layout="wide"
)

st.title("🤖 Multi-Modal Chatbot")

# ---------------- TEXT CHAT ---------------- #

st.header("💬 Chat with Gemini")

question = st.text_input("Ask me anything")

if st.button("Ask"):

    if question:

        with st.spinner("Thinking..."):

            answer = chat_with_gemini(question)

        st.success(answer)

st.divider()

# ---------------- IMAGE CHAT ---------------- #

st.header("🖼️ Image Understanding")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

image_prompt = st.text_input(
    "Ask something about the uploaded image"
)

if uploaded_image:

    image = Image.open(uploaded_image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Image"):

        with st.spinner("Analyzing image..."):

            response = analyze_image(image, image_prompt)

        st.success(response)

        st.divider()

st.header("🎨 Image Generation")

image_prompt = st.text_input(
    "Describe the image you want to generate"
)

if st.button("Generate Image"):

    if image_prompt:

        with st.spinner("Generating image..."):

            generated = generate_image(image_prompt)
            st.write(generated)

        st.image(
            "generated_image",
            caption="Generated Image",
            use_container_width=True
        )


        
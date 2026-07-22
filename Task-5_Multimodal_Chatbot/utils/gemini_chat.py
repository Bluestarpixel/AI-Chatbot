import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text


def analyze_image(image, prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[prompt, image],
    )

    return response.text

def generate_image(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-image",
        contents=prompt,
    )

    print(response)
    print(type(response))

    return response
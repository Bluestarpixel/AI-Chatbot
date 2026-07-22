import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from langdetect import detect

# Load environment variables
load_dotenv()

# Initialize Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def multilingual_chat(user_message):
    """
    Detects the user's language and generates a response
    in the same language using Gemini.
    """

    # Detect language
    try:
        language = detect(user_message)
    except Exception:
        language = "en"

    # Prompt for Gemini
    prompt = f"""
You are a multilingual AI assistant.

Instructions:
- Detect the language of the user's message.
- Reply ONLY in the same language.
- If the user changes language in a later message, switch automatically.
- Be natural, polite, and culturally appropriate.
- Keep answers clear and helpful.

User Message:
{user_message}
"""

    # Retry up to 3 times if Gemini is temporarily busy
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return response.text, language

        except errors.ServerError:
            if attempt < 2:
                time.sleep(3)
            else:
                return (
                    "⚠️ Gemini servers are currently busy. Please try again in a few minutes.",
                    language,
                )

        except Exception as e:
            return (
                f"❌ Error: {str(e)}",
                language,
            )
import ollama

def explain_concept(question):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": f"Explain this computer science concept in simple words: {question}"
            }
        ]
    )

    return response["message"]["content"]
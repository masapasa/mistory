# Synchronous Example
from mistralai import Mistral
import os

def chat():
    s = Mistral(
        api_key=os.getenv("MISTRAL_API_KEY", ""),
    )

    user_input = input("Enter your question: ")

    res = s.chat.complete(model="mistral-small-latest", messages=[
        {
            "content": user_input,
            "role": "user",
        },
    ])

    if res is not None:
        return (res['choices'][0]['message']['content'])  # handle response
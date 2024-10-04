import os
from groq import Groq  # Make sure to install the Groq library
from src.prompt import system_instruction

# Initialize the Groq client with the API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

messages = [
    {"role":"system","content":system_instruction}
]

def ask_order(message,model="gemma2-9b-it",temperature=0.7):
    response=client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content
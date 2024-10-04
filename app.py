import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # we send message through app interface
    # Your custom logic goes here...
    messages.append({"role":"user","content":message.content})
    response=ask_order(messages)
    messages.append({"role":"assistant", "content":response})
    # storing the content that we get from ask_order function

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()

from groq import Groq
from Interfaces.IApiKey import client

def AskGpt(userMessage, aiModel):                               #method to use in bot to pass the message from the user and return the answer from an AI model
    chat_completion = client.chat.completions.create(
        messages=[
                {
                "role": "user",
                "content": f"{userMessage}",
                }
            ],
        model=aiModel,
        )
    replyMessage = chat_completion.choices[0].message.content
    return replyMessage

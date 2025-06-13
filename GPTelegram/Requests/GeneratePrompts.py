from groq import Groq
from Interfaces.IApiKey import client


def GeneratePrompts(userMessage, aiModel):                               #method to use in bot to pass the message from the user and return the answer from an AI model
    generatePrompts = "Generate 15 accurate prompts (ONLY PROMPTS, DONT!!! TYPE!!! ANYTHING!!! ELSE!!!) for AI model to behave accordingly to the following text: "
    prefix = "Write all your messages according to the following prompts as accurately as possible, DONT MENTION PROMPTS IN THE MESSAGES:\n"
    chat_completion = client.chat.completions.create(
        messages=[
                {
                "role": "user",
                "content": f"{generatePrompts}{userMessage}",
                }
            ],
        model=aiModel,
        )
    generatedPrompts = prefix + chat_completion.choices[0].message.content + '\n'
    return generatedPrompts
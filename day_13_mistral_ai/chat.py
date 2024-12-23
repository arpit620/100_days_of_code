import os
from mistralai import Mistral

print("Hello, Mistral AI!")
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

print("Hello, Mistral AI 1!")
chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print("Hello, Mistral AI 2!")
print(chat_response.choices[0].message.content)
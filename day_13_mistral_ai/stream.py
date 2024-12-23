import os
from mistralai import Mistral

print("Hello 1")
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

print("Hello 2")
stream_response = client.chat.stream(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print("Hello 3")
for chunk in stream_response:
    print(chunk.data.choices[0].delta.content)

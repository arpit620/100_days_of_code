import os
from openai import OpenAI

client = OpenAI(
    base_url="https://glhf.chat/api/openai/v1",
    api_key=os.environ.get("GLHF_CHAT_API"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke",
        }
    ],
    model="hf:meta-llama/Llama-3.2-90B-Vision-Instruct",
)

print(chat_completion)
print("----------------")
print(chat_completion.choices[0].message.content)

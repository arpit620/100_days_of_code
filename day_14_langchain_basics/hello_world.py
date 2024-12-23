from langchain import LangChain
from mistral import MistralAI
import os

mistral_api_key = os.getenv('MISTRAL_API_KEY')

if mistral_api_key:
    print(f"MISTRAL_API_KEY: {mistral_api_key}")
else:
    print("MISTRAL_API_KEY is not set")

# Initialize LangChain and Mistral AI
langchain = LangChain()

# Initialize LangChain and Mistral AI with model specification
model_name = "open-mistral-nemo"  # Replace with the desired model name
mistral_ai = MistralAI(api_key=mistral_api_key, model=model_name)

def chat_with_mistral(prompt):
    response = mistral_ai.generate_response(prompt)
    return response

if __name__ == "__main__":
    user_input = input("You: tell me a joke")
    response = chat_with_mistral(user_input)
    print(f"Mistral AI: {response}")

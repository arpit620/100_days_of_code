from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage

# Initialize the chat model
chat = ChatMistralAI(model="mistral-small-latest")

# Prepare messages
messages = [HumanMessage(content="say a brief hello")]

# Invoke the chat model
response = chat.invoke(messages)
print(response)
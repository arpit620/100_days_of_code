# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
# from langchain_openai import OpenAI
from langchain.chains import LLMChain #, RunnableSequence
from langchain.prompts import PromptTemplate
import os

# Initialize the OpenAI API with your API key, base URL, and model name
GLHF_CHAT_API = os.environ.get("GLHF_CHAT_API")
BASE_URL = os.environ.get("BASE_URL", "https://glhf.chat/api/openai/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct")
openai_api_key = GLHF_CHAT_API
llm = OpenAI(api_key=openai_api_key, base_url=BASE_URL, model_name=MODEL_NAME)

# Define a prompt template
prompt = PromptTemplate(input_variables=["name"], template="Hello, {name}! How can I assist you today?")

# Create a RunnableSequence with the prompt and the OpenAI LLM
# chain = RunnableSequence([prompt, llm])
chain = prompt | llm

# Run the chain with an example input
response = chain.invoke({"name": "Joe"})
print(response)


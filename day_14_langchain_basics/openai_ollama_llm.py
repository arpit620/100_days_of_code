from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

information = """
Elon Musk is a renowned entrepreneur, visionary, and business magnate known for his groundbreaking contributions to the fields of technology and innovation.
He is the founder, CEO, and Chief Engineer of SpaceX, a private aerospace manufacturer revolutionizing space transportation.
Musk is also the co-founder and CEO of Tesla, Inc., leading the way in electric vehicle manufacturing and sustainable energy solutions.
His entrepreneurial journey includes co-founding companies like PayPal, Neuralink, and The Boring Company, each addressing significant technological challenges.
Musk's relentless pursuit of innovation and his ambitious projects have made him a prominent figure in the business world, shaping the future of transportation, energy, and space exploration.
"""

if __name__ == "__main__":
    load_dotenv()
    # openai_api_key = os.environ['OPENAI_API_KEY']
    
    # Initialize the OpenAI LLM with the API key
    GLHF_CHAT_API = os.environ.get("GLHF_CHAT_API")
    BASE_URL = os.environ.get("BASE_URL", "https://glhf.chat/api/openai/v1")
    MODEL_NAME = os.environ.get("MODEL_NAME", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct")
    openai_api_key = GLHF_CHAT_API
    # llm = ChatOpenAI(api_key=openai_api_key, base_url=BASE_URL, model_name=MODEL_NAME)
    # llm = ChatOllama(model="llama3.2")
    llm = ChatMistralAI(model_name="mistral-large-latest", temperature=0.0)
    
    
    # Example summary input
    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    # chain = summary_prompt_template | llm
    chain = summary_prompt_template | llm | StrOutputParser()
    response = chain.invoke(input={"information": information})
    
    # Print the response
    print(response)


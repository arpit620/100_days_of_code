from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from utils.output_parsers import summary_parser
import os

def openai_supported_call():
    GLHF_CHAT_API = os.environ.get("GLHF_CHAT_API")
    BASE_URL = os.environ.get("BASE_URL", "https://glhf.chat/api/openai/v1")
    MODEL_NAME = os.environ.get("MODEL_NAME", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct")
    openai_api_key = GLHF_CHAT_API
    llm = ChatOpenAI(api_key=openai_api_key, base_url=BASE_URL, model_name=MODEL_NAME)
    return llm

def get_summary_chain() -> RunnableSequence:
    summary_template = """
         given the information about a person from Wikipedia {information} I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = openai_supported_call()

    return summary_prompt_template | llm | summary_parser
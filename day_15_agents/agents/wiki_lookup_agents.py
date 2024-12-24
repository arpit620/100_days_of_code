import os

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily

load_dotenv()

def openai_supported_call():
    GLHF_CHAT_API = os.environ.get("GLHF_CHAT_API")
    BASE_URL = os.environ.get("BASE_URL", "https://glhf.chat/api/openai/v1")
    MODEL_NAME = os.environ.get("MODEL_NAME", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct")
    openai_api_key = GLHF_CHAT_API
    llm = ChatOpenAI(api_key=openai_api_key, base_url=BASE_URL, model_name=MODEL_NAME)
    return llm


def lookup(name: str, mock : bool = False) -> str:

    if not mock:
        llm = openai_supported_call()
        template = """given the full name {name_of_person} I want you to get me a link to their Wikipedia page.
                            Your answer should contain only a URL"""

        prompt_template = PromptTemplate(
            template=template, input_variables=["name_of_person"]
        )
        tools_for_agent = [
            Tool(
                name="Crawl Google for Wikipedia page",
                func=get_profile_url_tavily,
                description="useful for when you need get the Wikipedia Page URL",
            )
        ]

        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

        result = agent_executor.invoke(
            input={"input": prompt_template.format_prompt(name_of_person=name)}
        )

        wikipedia_url = result["output"]
    else:
        print("Mocking the lookup")
        wikipedia_url = "https://en.wikipedia.org/wiki/Elon_Musk"
    return wikipedia_url


if __name__ == "__main__":
    name = "Elon Musk"
    print(lookup(name))


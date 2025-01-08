from typing import Union, List
import re
import os
from dotenv import load_dotenv
from langchain.agents import tool
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain_openai import ChatOpenAI
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
from langchain.tools import Tool
from langchain.tools.render import render_text_description
from openai import OpenAI

from callbacks import AgentCallbackHandler


load_dotenv()


@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}")
    text = text.strip("'\n").strip(
        '"'
    )  # stripping away non alphabetic characters just in case

    return len(text)


def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool wtih name {tool_name} not found")

def openai_supported_call():
    GLHF_CHAT_API = os.environ.get("GLHF_CHAT_API")
    BASE_URL = os.environ.get("BASE_URL", "https://glhf.chat/api/openai/v1")
    MODEL_NAME = os.environ.get("MODEL_NAME", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct")
    openai_api_key = GLHF_CHAT_API
    llm = ChatOpenAI(
            api_key=openai_api_key, 
            base_url=BASE_URL, 
            model_name=MODEL_NAME,
            temperature=0,
            stop=["\nObservation", "Observation"],
            callbacks=[AgentCallbackHandler()],
            )
    return llm

def github_openai_supported_call():
    openai_api_key = os.environ.get("GITHUB_TOKEN")
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o-mini"
    llm = ChatOpenAI(
            api_key=openai_api_key, 
            base_url=endpoint, 
            model=model_name,
            temperature=0,
            stop=["\nObservation", "Observation"],
            callbacks=[AgentCallbackHandler()],
            )
    return llm


def mistral_ai():
    MISTRAL_CHAT_API = os.environ.get("MISTRAL_API_KEY")
    llm = ChatMistralAI(
        api_key=MISTRAL_CHAT_API,
        model="mistral-large-latest",
        temperature=0,
        stop=["\nObservation", "Observation"],
        callbacks=[AgentCallbackHandler()],
    )
    return llm

if __name__ == "__main__":
    print("Hello ReAct LangChain!")
    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought: {agent_scratchpad}
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    # llm = openai_supported_call()
    # llm = mistral_ai()
    llm = github_openai_supported_call()

    intermediate_steps = []
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
        }
        | prompt
        | llm
        | ReActSingleInputOutputParser()
    )

    agent_step = ""
    while not isinstance(agent_step, AgentFinish):
        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {
                "input": "What is the length of the word: HELLO",
                "agent_scratchpad": intermediate_steps,
            }
        )
        print(agent_step)

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_use = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input

            observation = tool_to_use.func(str(tool_input))
            print(f"{observation=}")
            intermediate_steps.append((agent_step, str(observation)))

    if isinstance(agent_step, AgentFinish):
        print(agent_step.return_values)

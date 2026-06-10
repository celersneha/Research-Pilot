from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="qwen/qwen3-32b", temp=0)

# first agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools = [web_search]
    )


# second agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )
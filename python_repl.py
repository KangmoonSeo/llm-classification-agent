import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms.openai import OpenAI

os.environ["SERPAPI_API_KEY"] = "e32618669d79a3b7abb62285b5cf74b8dae599c9ed6648d1113643396772cbc5"
OpenAI(api_key="EMPTY", base_url="http://165.246.21.213:10103/v1")

tools = load_tools(
    tool_names=["serpapi", "llm-math", "python_repl"],
    llm=OpenAI(temperature=0, api_key="EMPTY", base_url="http://165.246.21.213:10103/v1"),
)

agent = initialize_agent(
    agent="zero-shot-react-description",
    llm=OpenAI(temperature=0, api_key="EMPTY", base_url="http://165.246.21.213:10103/v1"),
    tools=tools,
    verbose=True,
)

agent.run("123*4를 계산해주세요.")
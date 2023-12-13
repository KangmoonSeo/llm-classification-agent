import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_base_url = os.getenv("OPENAI_BASE_URL")
serpapi_api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_BASE_URL"] = openai_base_url
os.environ["SERPAPI_API_KEY"] = serpapi_api_key

openai = OpenAI(temperature=0, api_key=openai_api_key, base_url=openai_base_url)

tools = load_tools(tool_names=["serpapi", "llm-math"], llm=openai)

agent = initialize_agent(
    agent="zero-shot-react-description",
    llm=openai,
    tools=tools,
    verbose=True,
)

agent.run("123*4를 계산해주세요.")

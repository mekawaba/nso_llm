import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.tools.base import BaseTool
from langchain.agents import initialize_agent
from langchain.agents import AgentType

class HelloTool(BaseTool):
    """Tool that generates a personalized hello message."""

    name = "HelloTool"
    description = (
        "A tool that generates a personalized hello message. "
        "Input should be a name string."
    )

    def _run(self, name: str = None) -> str:
        return f"Hello {name}!"

    async def _arun(self, name: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(name)


#tool_names = [HelloTool()]
#tools = load_tools(tool_names)
tools = [HelloTool()]

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("""Hi,Tom!""")
from strands import Agent
from strands_tools import http_request

agent = Agent(
    model="us.anthropic.claude-sonnet-4-6",
    tools=[
        http_request
    ]
    )

agent("""
   Using the website https://en.wikipedia.org/wiki/Dungeons_%26_Dragons tell me the name of the designers of
   Dungeons and Dragons.
    """
    )


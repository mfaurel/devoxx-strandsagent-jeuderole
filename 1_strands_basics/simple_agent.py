from strands import Agent

agent = Agent(
    model="us.anthropic.claude-sonnet-4-6",
    system_prompt="You are a game master for a Dungeon & Dragon game"
)

agent("Hi, I am an adventurer ready for adventure!")

import logging

from strands import Agent

agent = Agent()

logging.basicConfig(level=logging.INFO)

agent = Agent(system_prompt="You are a game master for a Dungeon & Dragon game")

agent("Hi, I am an adventurer ready for adventure!")

from strands import Agent, tool


@tool
def roll_dice(faces: int = 6) -> int:
    """
    🎲 Roll a dice with a specified number of faces.

    Args:
        faces: The number of faces on the dice (default: 6). Must be at least 1.

    Returns:
        A random integer between 1 and faces (inclusive).
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)



dice_master = Agent(
    model="us.anthropic.claude-sonnet-4-6",
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

# Test your dice master's abilities
dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")


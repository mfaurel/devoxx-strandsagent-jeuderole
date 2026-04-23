from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

def main():
    print("\nConnecting to D&D Dice Roll MCP Server...")
    mcp_client = MCPClient(lambda: streamablehttp_client("http://localhost:8080/mcp"))

    try:
        with mcp_client:
            gamemaster = Agent(
                model="us.anthropic.claude-sonnet-4-6",
                system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
                You speak with theatrical flair and always announce dice rolls with appropriate drama.
                You know all about D&D mechanics, always use the appropriate tools when applicable - never make up results!""",
                tools=mcp_client.list_tools_sync()
            )
            
            while True:
                user_input = input("\n🎲 Your request: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("🎭 May fortune favor your future adventures!")
                    break

                print("\n🎲 Rolling the dice of fate...\n")
                gamemaster(user_input)

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("💡 Make sure the dice service is running: python dice_roll_mcp_server.py")

if __name__ == "__main__":
    main()

from agents.email_agent import get_email_tool
from agents.meeting_agent import get_meeting_tool
from tools.email_tools import get_recent_emails
from tools.meeting_tools import schedule_meeting
from llm.azure_openai import chat_with_tools

def handle_tool_call(tool_call):
    name = tool_call.function.name
    arguments = tool_call.function.arguments
    import json
    args = json.loads(arguments)
    if name == "get_recent_emails":
        emails = get_recent_emails(args.get("count", 3))
        return {"emails": emails}
    elif name == "schedule_meeting":
        result = schedule_meeting(args["date"], args["time"], args["duration"])
        return result
    else:
        return {"error": "Unknown tool"}

def main():
    print("Welcome to the Agentic AI Demo!")
    
    user_query = input("You: ")

    # Both tools available for demo
    tools = [get_email_tool(), get_meeting_tool()]
    messages = [
        {"role": "system", "content": "You are an assistant that can help with emails and meetings."},
        {"role": "user", "content": user_query}
    ]
    response = chat_with_tools(messages, tools)
    message = response.choices[0].message

    # Check if tool call is required
    if message.tool_calls:
        # First, add the assistant message with tool calls to the conversation
        messages.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                } for tool_call in message.tool_calls
            ]
        })
        
        # Then add tool responses
        for tool_call in message.tool_calls:
            tool_response = handle_tool_call(tool_call)
            # Add tool response to messages and get final answer

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(tool_response)
            })

        # Get final response after tool call

        final_response = chat_with_tools(messages, tools)
        print("Agent:", final_response.choices[0].message.content)
    else:
        print("Assistant:", message.content)

if __name__ == "__main__":
    main() 
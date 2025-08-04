import json
import openai
from config import OPENAI_API_KEY, DEFAULT_MODEL
from tools import calculator_tool, get_current_time, web_search

openai.api_key = OPENAI_API_KEY

# Tool definitions for GPT
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator_tool",
            "description": "Perform mathematical calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get current time in a timezone",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "Timezone string like UTC or Asia/Tokyo"
                    }
                },
                "required": ["timezone"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web and return top results",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search terms"},
                    "num_results": {"type": "integer", "description": "Number of results (1-5)"}
                },
                "required": ["query"]
            }
        }
    }
]


def call_tool(name, arguments):
    if name == "calculator_tool":
        return calculator_tool(arguments.get("expression", ""))
    elif name == "get_current_time":
        return get_current_time(arguments.get("timezone", "UTC"))
    elif name == "web_search":
        return web_search(arguments.get("query", ""), arguments.get("num_results", 3))
    return "Unknown tool"


def chat_loop():
    print("ChatBot ready! Type 'exit' to quit.")
    messages = [{"role": "system", "content": "You are a helpful assistant. Call one or more tools as needed."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        # First GPT response (tool calls or text)
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        msg = response.choices[0].message

        # If GPT calls any tools
        if msg.get("tool_calls"):
            messages.append(msg)
            for tool_call in msg["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                args = json.loads(tool_call["function"]["arguments"])
                tool_call_id = tool_call.get("id")
                tool_result = call_tool(tool_name, args)
                print(f"Tool used: {tool_name}\nResult: {tool_result}")

                # Add a tool response for each call
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call_id,
                    "content": tool_result
                })

            # After responding to all tool calls, get final answer
            followup = openai.ChatCompletion.create(
                model=DEFAULT_MODEL,
                messages=messages
            )
            final_msg = followup.choices[0].message
            print(f"Bot: {final_msg['content']}")
            messages.append(final_msg)

        else:
            print(f"Bot: {msg['content']}")
            messages.append(msg)


if __name__ == "__main__":
    chat_loop()

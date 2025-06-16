import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_API_BASE")
)

ENGINE = os.getenv("AZURE_OPENAI_ENGINE")

def chat_with_tools(messages, tools, tool_choice="auto"):

    response = client.chat.completions.create(
        model=ENGINE,
        messages=messages,
        tools=tools,
        tool_choice=tool_choice
    )
    return response 
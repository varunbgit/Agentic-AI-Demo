# Agentic AI Demo

A hands-on demonstration of AI agents using Azure OpenAI with function calling capabilities.

## Features

- **Email Agent**: Fetches and summarizes recent emails
- **Meeting Agent**: Schedules meetings in your calendar
- **Modular Architecture**: Clean separation of concerns with tools, agents, and LLM integration

## Setup

1. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   Create a `.env` file in the `src` directory with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_API_KEY=your-azure-openai-key-here
   AZURE_OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2024-08-01-preview
   AZURE_OPENAI_ENGINE=gpt-4o-mini
   

3. **Run the Demo**
   ```bash
   python main.py
   ```

## Usage Examples

Try these queries when running the demo:

- "What's new in my inbox?"
- "Show me my recent emails"
- "Schedule a meeting tomorrow at 3pm for 30 minutes"
- "Book a 1-hour meeting for next Friday at 2pm"

## Architecture

```
src/
├── agents/          # Agent definitions (tool configurations)
├── tools/           # Tool implementations (mocked APIs)
├── llm/            # Azure OpenAI integration
├── main.py         # Entry point and orchestration
└── requirements.txt
```

## Notes

- This demo uses mocked data for emails and calendar
- Perfect for presentations and learning about agentic AI
- Easy to extend with additional tools and agents 
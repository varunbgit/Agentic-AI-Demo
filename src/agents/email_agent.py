def get_email_tool():
    return {
        "type": "function",
        "function": {
            "name": "get_recent_emails",
            "description": "Fetches the most recent emails for the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer",
                        "description": "Number of recent emails to fetch"
                    }
                },
                "required": ["count"]
            }
        }
    } 
def get_meeting_tool():
    return {
        "type": "function",
        "function": {
            "name": "schedule_meeting",
            "description": "Schedules a meeting in the user's calendar.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "Date of the meeting (YYYY-MM-DD)"},
                    "time": {"type": "string", "description": "Time of the meeting (HH:MM)"},
                    "duration": {"type": "integer", "description": "Duration in minutes"}
                },
                "required": ["date", "time", "duration"]
            }
        }
    } 
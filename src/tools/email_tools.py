def get_recent_emails(count):
    # Mocked email data
    emails = [
        {"from": "boss@company.com", "subject": "Project Update", "body": "Please send the latest report."},
        {"from": "hr@company.com", "subject": "Policy Change", "body": "New leave policy attached applicable from 2 may 2025. kindly check "},
        {"from": "colleague@company.com", "subject": "Lunch?", "body": "Want to grab lunch today?"},
    ]
    return emails[:count] 
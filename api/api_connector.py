# api/api_connector.py
# Just a testing script for api client logic 

import api_client

def run(action: str):
    if action == "test_note":
        print(api_client.add_note("Test Title", "Test Desc"))

    elif action == "test_pomo":
        print(api_client.add_pomo("Focus Session", 25))

    elif action == "test_expense":
        print(api_client.add_expense(120, "Testing Expense"))

    elif action == "view_notes":
        print(api_client.view_notes())

    elif action == "test_review":
        print(api_client.get_review())

    else:
        print(f"❓ Unknown action: {action}")

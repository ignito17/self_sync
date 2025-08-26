# modules/stats_viewer.py
# A row is a dict with ("Column":value)

import sqlite3
from datetime import datetime
from db_engine.engine import CSVEngine

engine=CSVEngine()  # Engine Object

def show_review():
    today = datetime.now().date().isoformat()
    
    print("\n📊 Daily Review")
    print("=" * 30)

    print(f"✅ Pomodoro:")
    # Pomodoro summary
    row_list=engine["pomos"].read_all()
    for row in row_list:
        print(row)

    print(f"💸 Expenses: ₹")
    # Expense summary
    row_list=engine["expenses"].read_all()
    for row in row_list:
        print(row)
    # print(f"💸 Expenses: ₹{expense_total or 0:.2f}")

    # Diary entries
    print("\n📝 Notes:")
    row_list=engine["notes"].read_all()
    for row in row_list:
        print(row)

    print("=" * 30)

def send_review(days=1):
    all_data={f"✅ Pomodoro:":[row for row in engine["pomos"].read_all()],
              f"💸 Expenses: ₹":[row for row in engine["expenses"].read_all],
              f"📝 Notes:":[row for row in engine["notes"].read_all]}
    return all_data
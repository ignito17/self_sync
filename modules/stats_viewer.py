# modules/stats_viewer.py

import sqlite3
from datetime import datetime

DB_PATH = "db/data.sqlite"

def show_review():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    today = datetime.now().date().isoformat()

    print("\n📊 Daily Review")
    print("=" * 30)

    # Pomodoro summary
    c.execute("""
        SELECT SUM(minutes), topic 
	FROM pomo_sessions
        WHERE DATE(timestamp) = ?
	GROUP BY pomo_sessions.topic
    """, (today,))
    pomo_total = c.fetchone()[0]
    print(f"✅ Pomodoro: {pomo_total or 0} minutes for topic")

    # Expense summary
    c.execute("""
        SELECT SUM(amount) FROM expenses
        WHERE DATE(timestamp) = ?
    """, (today,))
    expense_total = c.fetchone()[0]
    print(f"💸 Expenses: ₹{expense_total or 0:.2f}")

    # Diary entries
    print("\n📝 Notes:")
    c.execute("""
        SELECT * FROM diary_entries
        WHERE DATE(timestamp) = ?
    """, (today,))
    notes = c.fetchall()
    if notes:
        for i, note in enumerate(notes, 1):
            print(f"  {i}. {note[0],note[1],note[2:]}")
    else:
        print("  No diary notes today.")

    print("=" * 30)
    conn.close()

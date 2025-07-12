# query_db.py

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "db", "data.sqlite"))

def show_notes(limit=5):
    print("\n📝 Latest Notes:")
    with sqlite3.connect(DB_PATH) as conn:
        for row in conn.execute("SELECT id, title, timestamp FROM diary_entries ORDER BY timestamp DESC LIMIT ?", (limit,)):
            print(f"  [{row[0]}] {row[1]} — {row[2][:19]}")

def show_pomos(limit=5):
    print("\n⏱️ Latest Pomos:")
    with sqlite3.connect(DB_PATH) as conn:
        for row in conn.execute("SELECT id, topic, minutes, timestamp FROM pomo_sessions ORDER BY timestamp DESC LIMIT ?", (limit,)):
            print(f"  [{row[0]}] {row[2]} min — {row[1]} @ {row[3][:19]}")

def show_expenses(limit=5):
    print("\n💸 Latest Expenses:")
    with sqlite3.connect(DB_PATH) as conn:
        for row in conn.execute("SELECT id, amount, desc, timestamp FROM expenses ORDER BY timestamp DESC LIMIT ?", (limit,)):
            print(f"  [{row[0]}] ₹{row[1]} — {row[2][:40]} @ {row[3][:19]}")

if __name__ == "__main__":
    show_notes()
    show_pomos()
    show_expenses()

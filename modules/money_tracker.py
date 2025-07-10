# modules/money_tracker.py

import sqlite3
from datetime import datetime

DB_PATH = "db/data.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            desc TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_expense(amount, desc):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses (amount, desc, timestamp) VALUES (?, ?, ?)",
        (amount, desc, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    print(f"💸 Expense of ₹{amount} logged for '{desc}'.")

# modules/money_tracker.py

# import sqlite3                    # Legacy from self_sync_core-a1
import os
from datetime import datetime
from db_engine.engine import CSVEngine

# DB_PATH = "db/data.sqlite"        # Legacy from self_sync_core-a1
# Instantiate the engine with  desired path
# passed as CSVEngine(schema_dir="/*.json",data_dir="/*.csv")
engine = CSVEngine()                # Uses Default Arguments

def add_expense(amount, description):
    """Add a new expense row using the data model abstraction."""
    row = {
        "amount": float(amount),
        "description": description.strip()
    }
    engine["expenses"].insert(row)
    print(f"💸 Expense of ₹{amount:.2f} logged for '{description[:40]}'.")

#                                   # Legacy from self_sync_core-a1
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS expenses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             amount REAL NOT NULL,
#             desc TEXT NOT NULL,
#             timestamp TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()
#                                   # Legacy from self_sync_core-a1

#                                 # Legacy from self_sync_core-a1  
# def add_expense(amount, desc):
#     init_db()
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute(
#         "INSERT INTO expenses (amount, desc, timestamp) VALUES (?, ?, ?)",
#         (amount, desc, datetime.now().isoformat())
#     )
#     conn.commit()
#     conn.close()
#     print(f"💸 Expense of ₹{amount} logged for '{desc}'.")
#                               # Legacy from self_sync_core-a1


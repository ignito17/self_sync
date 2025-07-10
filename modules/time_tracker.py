# modules/time_tracker.py

import sqlite3
from datetime import datetime

DB_PATH = "db/data.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pomo_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            minutes INTEGER NOT NULL,
	    topic TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_pomo(minutes,topic):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO pomo_sessions (minutes,topic,timestamp) VALUES (?, ?, ?)",
        (minutes,topic, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    print(f"✅ Pomodoro of {minutes} minutes of {topic} logged.")

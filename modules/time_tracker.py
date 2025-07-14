# modules/time_tracker.py

import os
from datetime import datetime
from db_engine.engine import CSVEngine

engine=CSVEngine()

def add_pomo(minutes,topic):
    row={
        "minutes":int(minutes),
        "topic":topic.strip()
    }
    engine["pomos"].insert(row)
    print(f"✅ Pomodoro of {minutes} minutes of '{topic}' logged.")

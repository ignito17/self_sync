# modules/diary_logger.py

# import sqlite3				#legacy from self_sync_core-a1
import os
from datetime import datetime
from db_engine.engine import CSVEngine
# DB_PATH="db/data.sqlite"

def add_note(title,desc):
	row={
		"title":title.strip(),
		"description":desc.strip()
	}
	
	print(f"📝 Note saved:\n")
	print(f"Title:-{title},Description:-{desc[:40]}{'...' if len(desc) > 40 else desc}")

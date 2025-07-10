# modules/diary_logger.py

import sqlite3
from datetime import datetime
DB_PATH="db/data.sqlite"

def init_db():
	conn=sqlite3.connect(DB_PATH)
	c=conn.cursor()
	c.execute("""
	CREATE TABLE IF NOT EXISTS diary_entries (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	timestamp TEXT NOT NULL)
	""")
	conn.commit()
	conn.close()

def add_note(title,desc):
	init_db()
	conn=sqlite3.connect(DB_PATH)
	c=conn.cursor()
	c.execute("""INSERT INTO diary_entries (title,description,timestamp)
		VALUES (?,?,?)""",(title,desc,datetime.now().isoformat())
		)
	conn.commit()
	conn.close()
	print(f"📝 Note saved:\n")
	print(f"Title:-{title},Description:-{desc[:40]}{'...' if len(desc) > 40 else desc}")

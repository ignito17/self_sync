import sqlite3
import os

db_files = ["data.sqlite", "sqlite.db", "sqlite.db.old"]

for db in db_files:
    if not os.path.exists(db):
        continue
    print(f"\nChecking DB: {db}")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    if tables:
        print("Tables found:", tables)
        for table_name, in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"  → {table_name}: {count} rows")
    else:
        print("No tables found.")
    conn.close()

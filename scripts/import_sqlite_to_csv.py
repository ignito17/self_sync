# scripts/import_sqlite_to_csv.py

import sqlite3
import os
from db_engine.engine import engine

# ---- Config ----
sqlite_db_path = "db/data.sqlite"
table_map = {
    "expenses": "expenses",
    "diary_entries": "notes",
    "pomo_sessions": "pomos"
}

# ---- Connect to SQLite ----
if not os.path.exists(sqlite_db_path):
    raise FileNotFoundError(f"{sqlite_db_path} not found.")

conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()

# ---- For each table ----
for sqlite_table, csv_table in table_map.items():
    print(f"Importing {sqlite_table} → {csv_table}...")

    cursor.execute(f"SELECT * FROM {sqlite_table}")
    rows = cursor.fetchall()

    col_names = [desc[0] for desc in cursor.description]
    for row in rows:
        row_dict = dict(zip(col_names, row))

        # Drop existing ID and timestamp — let CSVEngine handle it
        row_dict.pop("id", None)
        row_dict.pop("timestamp", None)

        # Insert using CSV Engine API
        engine[csv_table].insert(row_dict)

    print(f"✅ {len(rows)} rows imported.")

conn.close()

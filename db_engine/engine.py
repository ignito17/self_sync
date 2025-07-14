# db_engine/engine.py

import os, csv, json
from datetime import datetime

# Table Object
class CSVTable:
    def __init__(self, table_name, schema_dir, data_dir):
        self.table_name = table_name
        self.schema_path = os.path.join(schema_dir, f"{table_name}.json")
        self.data_path = os.path.join(data_dir, f"{table_name}.csv")

        self.schema = self._load_schema()
        self.columns = self.schema["columns"]
        self.auto_increment = self.schema.get("auto_increment", False)
        self.timestamp_fields = self.schema.get("timestamp_fields", [])

        self._init_table_file()

    # Private Methods --Python Style
    def _load_schema(self):
        with open(self.schema_path) as f:
            return json.load(f)

    def _init_table_file(self):
        if not os.path.exists(self.data_path):
            with open(self.data_path, "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.columns)
                writer.writeheader()

    def _read_all_rows(self):
        with open(self.data_path, newline='') as f:
            return list(csv.DictReader(f))
    
    # Public Methods, Java style :)
    def insert(self, row_dict):
        # handle auto-increment
        if self.auto_increment:
            rows = self._read_all_rows()
            last_id = int(rows[-1]["id"]) if rows else 0
            row_dict["id"] = str(last_id + 1)

        # handle timestamp fields
        now = datetime.now().isoformat()
        for field in self.timestamp_fields:
            row_dict[field] = now

        # enforce column structure
        final_row = {col: row_dict.get(col, "") for col in self.columns}

        with open(self.data_path, "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.columns)
            writer.writerow(final_row)

    def read_all(self):
        return self._read_all_rows()

    def find_by_id(self, id_val):
        rows = self._read_all_rows()
        for row in rows:
            if row["id"] == str(id_val):
                return row
        return None

    def __repr__(self):
        return f"<CSVTable: {self.table_name}>"

# -- Engine Container
# -- This engine can be generalised for use with other 
# -- Directories or data fiels for imports and exports
# -- Just define schema_dir, data_dir of the hypothetical engine
class CSVEngine:
    def __init__(self, schema_dir="db_engine/schemas", data_dir="db_engine/data"):
        self.schema_dir = schema_dir
        self.data_dir = data_dir
        self.tables = {}
        self._load_tables()

    def _load_tables(self):
        for filename in os.listdir(self.schema_dir):
            if filename.endswith(".json"):
                table_name = filename[:-5]
                self.tables[table_name] = CSVTable(table_name, self.schema_dir, self.data_dir)

    def __getitem__(self, table_name):
        return self.tables.get(table_name)

# Global engine object
engine = CSVEngine()

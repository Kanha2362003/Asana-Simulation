import sqlite3

def get_connection(db_path):
    return sqlite3.connect(db_path)

def run_schema(conn, schema_path):
    with open(schema_path, "r") as f:
        conn.executescript(f.read())

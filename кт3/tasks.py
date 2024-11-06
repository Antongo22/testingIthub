import os
import sqlite3

def get_string_length(s: str) -> int:
    return len(s)

def save_string_to_file(s: str, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(s)

def create_connection(db_name: str) -> sqlite3.Connection:
    return sqlite3.connect(db_name)

def clear_database(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
    conn.commit()
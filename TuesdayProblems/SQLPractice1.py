import sqlite3

conn = sqlite3.connect("gradebook.db")

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    major Text,
    gpa REAL
)
"""
)

conn.commit()

print("Table created successfully.")



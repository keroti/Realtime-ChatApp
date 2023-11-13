import sqlite3

# Get the SQLite version
conn = sqlite3.connect('./db.sqlite3')  # Replace with the path to your database file
cursor = conn.cursor()
cursor.execute("SELECT sqlite_version();")
sqlite_version = cursor.fetchone()[0]
conn.close()

print(f"SQLite Version: {sqlite_version}")

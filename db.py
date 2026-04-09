import sqlite3
def get_connection():
    sqlite3.connect("db.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(is INTEGER PRIMARY_KEY, AUTOINCREMENT, username TEXT NOT NULL, email TEXT NOT NULL)
    """)
    conn.commit()
    conn.close()
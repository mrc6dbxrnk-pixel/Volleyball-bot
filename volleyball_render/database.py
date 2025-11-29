import sqlite3

def db():
    return sqlite3.connect("data/database.db")

def init_db():
    conn=db()
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER UNIQUE, username TEXT, full_name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS shifts (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time_label TEXT, price INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS registrations (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, shift_id INTEGER, status TEXT, paid INTEGER DEFAULT 0, screenshot_id TEXT, created_at TEXT)")
    conn.commit()
    conn.close()

import sqlite3

DB = "strava.db"

def get_conn():
    conn = sqlite3.connect(DB, timeout=30, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    # Activities
    c.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY,
        name TEXT,
        distance REAL,
        elevation REAL,
        moving_time REAL,
        gear_id TEXT,
        polyline TEXT
    )
    """)

    # Segments
    c.execute("""
    CREATE TABLE IF NOT EXISTS segments (
        id INTEGER,
        name TEXT,
        distance REAL,
        activity_id INTEGER
    )
    """)

    # Segments
    c.execute("""
    CREATE TABLE IF NOT EXISTS bikes (
        id INTEGER,
        name TEXT,
        distance REAL,
        activity_id INTEGER
    )
    """)

    conn.commit()
    conn.close()

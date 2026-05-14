import sqlite3

DB = "strava.db"

def get_conn():
    conn = sqlite3.connect(DB, timeout=30, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    # ActivityStats
    c.execute("""
        CREATE TABLE IF NOT EXISTS ActivityStats (
            biggest_ride_distance REAL,
    		biggest_climb_elevation_gain REAL,
            recent_ride_totals REAL,
            recent_run_totals REAL,
            recent_swim_totals REAL,
            ytd_ride_totals REAL,
            ytd_run_totals REAL,
            ytd_swim_totals REAL,
            all_ride_totals REAL,
            all_run_totals REAL,
            all_swim_totals REAL
        )
    """)

    # ActivityTotal
    c.execute("""
        CREATE TABLE IF NOT EXISTS ActivityTotal (
            count INTEGER,
    		distance REAL,
    		moving_time INTEGER,
    		elapsed_time INTEGER,
    		elevation_gain REAL,
    		achievement_count INTEGER
        )
    """)

    # DetailedGear
    c.execute("""
        CREATE TABLE IF NOT EXISTS DetailedGear (
            id TEXT,
    		resource_state INTEGER,
    		primary INTEGER,
    		name TEXT,
    		hours_total REAL,
    		hours_moving REAL,
    		distance REAL,
    		brand_name TEXT,
    		model_name TEXT,
    		frame_type INTEGER,
    		description TEXT,
        )
    """)

    # DetailedAthlete
    c.execute("""
        CREATE TABLE IF NOT EXISTS DetailedAthlete (
            id INTEGER,
    		resource_state INTEGER,
    		firstname TEXT,
    		lastname TEXT,
    		profile_medium TEXT,
    		profile TEXT,
    		city TEXT,
    		state TEXT,
    		country TEXT,
    		sex TEXT,
    		premium INTEGER,
    		summit INTEGER,
    		created_at TEXT,
    		updated_at TEXT,
    		follower_count INTEGER,
    		friend_count INTEGER,
    		measurement_preference TEXT,
    		ftp INTEGER,
    		weight REAL,
        )
    """)

    # DetailedClub
    c.execute("""
        CREATE TABLE IF NOT EXISTS DetailedClub (
            id INTEGER,
    		resource_state INTEGER,
    		name TEXT,
    		profile_medium TEXT,
    		cover_photo TEXT,
    		cover_photo_small TEXT,
    		sport_type TEXT,
    		city TEXT,
    		state TEXT,
    		country TEXT,
    		private INTEGER,
    		member_count INTEGER,
    		featured INTEGER,
    		verified INTEGER,
    		url TEXT,
    		membership TEXT,
    		admin INTEGER,
    		owner INTEGER,
    		following_count INTEGER
        )
    """)

    conn.commit()
    conn.close()

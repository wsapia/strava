from flask import Blueprint, session, jsonify
from services.strava import StravaClient
from db import get_conn

segments_bp = Blueprint('segments', __name__)

@segments_bp.route('/')
def all_segments():
    conn = get_conn()
    c = conn.cursor()

    rows = c.execute("""
        SELECT name, COUNT(*) 
        FROM segments 
        GROUP BY name 
        ORDER BY COUNT(*) DESC
    """).fetchall()

    conn.close()

    return jsonify([
        {"name": r[0], "times": r[1]} for r in rows
    ])
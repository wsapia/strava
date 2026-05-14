from flask import Blueprint, jsonify
from db import get_conn
from services.strava import StravaClient
from flask import session

bikes_bp = Blueprint('bikes', __name__)

@bikes_bp.route('/')
def bikes():

    conn = get_conn()
    c = conn.cursor()

    rows = c.execute("""
        SELECT gear_id, SUM(distance), SUM(moving_time), COUNT(*)
        FROM activities
        WHERE gear_id IS NOT NULL
        GROUP BY gear_id
    """).fetchall()

    client = StravaClient(session['token'])

    result = {}

    for r in rows:
        gid = r[0]
        gear = client.gear(gid)

        result[gid] = {
            "name": gear.get("name", "Unknown"),
            "distance": r[1],
            "hours": r[2] / 3600,
            "rides": r[3]
        }

    return jsonify(result)
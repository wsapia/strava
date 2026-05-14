from flask import Blueprint, session, jsonify
from db import get_conn
from sync import sync_activities

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/')
def activities():

    # ✅ sync only once per session
    # sync_activities(session['token'])

    conn = get_conn()
    c = conn.cursor()

    rows = c.execute("SELECT * FROM activities ORDER BY id DESC LIMIT 25").fetchall()

    conn.close()

    return jsonify([
        {
            "id": r[0],
            "name": r[1],
            "distance": r[2],
            "elevation": r[3],
            "time": r[4],
            "gear_id": r[5]
        } for r in rows
    ])

@activities_bp.route('/detail/<int:id>')
def detail(id):

    conn = get_conn()
    c = conn.cursor()

    row = c.execute("""
        SELECT id, name, polyline
        FROM activities
        WHERE id=?
    """, (id,)).fetchone()

    conn.close()

    if not row:
        return {"error": "Activity not found"}

    return {
        "id": row[0],
        "name": row[1],
        "polyline": row[2]
    }

@activities_bp.route('/sync')
def sync():
    sync_activities(session['token'])
    return {"status": "synced"}


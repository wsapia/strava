from flask import Blueprint, session, jsonify
from services.strava import StravaClient

streams_bp = Blueprint('streams', __name__)

@streams_bp.route('/<id>')
def streams(id):
    client = StravaClient(session['token'])
    return jsonify({
        "distance": data.get("distance", {}).get("data", []),
        "altitude": data.get("altitude", {}).get("data", []),
        "velocity": data.get("velocity_smooth", {}).get("data", []),
        "heartrate": data.get("heartrate", {}).get("data", [])
    })

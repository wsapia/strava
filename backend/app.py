import os
import logging
from flask import Flask, send_from_directory

from routes.auth import auth_bp
from routes.activities import activities_bp
from routes.bikes import bikes_bp
from routes.streams import streams_bp
from db import init_db

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__, static_folder=None)
app.secret_key = 'dev'

init_db()

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(activities_bp, url_prefix='/api/activities')
app.register_blueprint(bikes_bp, url_prefix='/api/bikes')
app.register_blueprint(streams_bp, url_prefix='/api/streams')

# Frontend routes
@app.route('/')
def root():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route('/ping')
def ping():
    return "pong"

@app.errorhandler(Exception)
def handle(e):
    logger.exception("Unhandled error")
    return {"error": str(e)}, 500
    
@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

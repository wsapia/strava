import os
import requests
from dotenv import load_dotenv
from flask import Blueprint, redirect, request, session

auth_bp = Blueprint('auth', __name__)

load_dotenv("../.env")

CLIENT_ID = os.environ["STRAVA_CLIENT_ID"]
CLIENT_SECRET = os.environ["STRAVA_CLIENT_SECRET"]

REDIRECT_URI = 'http://localhost:5000/callback'

@auth_bp.route('/login')
def login():
    url = (
        f"https://www.strava.com/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=read,read_all,profile:read_all,activity:read,activity:read_all"
    )
    return redirect(url)

@auth_bp.route('/callback')
def callback():
    code = request.args.get('code')

    token = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }
    ).json()

    session['token'] = token['access_token']
    return redirect('/')

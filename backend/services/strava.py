import requests

BASE = "https://www.strava.com/api/v3"

class StravaClient:
    def __init__(self, token):
        self.headers = {'Authorization': f'Bearer {token}'}

    def activities(self, page=1, per_page=25):
        r = requests.get(
            BASE + '/athlete/activities',
            headers=self.headers,
            params={'page': page, 'per_page': per_page}
        )

        try:
            data = r.json()
        except:
            return {"error": "Invalid JSON", "text": r.text}

        if r.status_code != 200:
            return {"error": r.status_code, "data": data}

        return data

    def gear(self, gid):
        return requests.get(f"{BASE}/gear/{gid}", headers=self.headers).json()

    def streams(self, aid):
        return requests.get(
            f"{BASE}/activities/{aid}/streams",
            headers=self.headers,
            params={'keys': 'distance,altitude', 'key_by_type': 'true'}
        ).json()
            
    def activity_full(self, id):
        r = requests.get(
            f"{BASE}/activities/{id}",
            headers=self.headers
        )

        try:
            data = r.json()
        except:
            return {"error": "Invalid JSON", "text": r.text}

        if r.status_code != 200:
            return {"error": r.status_code, "data": data}

        return data
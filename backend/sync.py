from services.strava import StravaClient
from db import get_conn

def sync_activities(token):

    client = StravaClient(token)
    page = 1

    while True:
        data = client.activities(page, 50)

        # ✅ VALIDATION
        if not isinstance(data, list):
            print("ERROR: activities API returned:", data)
            break

        if not data:
            break

        conn = get_conn()
        c = conn.cursor()

        for a in data:

            # ✅ SAFETY
            if not isinstance(a, dict) or 'id' not in a:
                print("Skipping invalid activity:", a)
                continue

            full = client.activity_full(a['id'])

            # ✅ VALIDATE FULL RESPONSE
            if not isinstance(full, dict):
                print("Invalid full activity:", full)
                continue

            polyline = full.get("map", {}).get("summary_polyline", "")

            c.execute("""
            INSERT OR IGNORE INTO activities
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                a['id'],
                a['name'],
                a['distance'],
                a['total_elevation_gain'],
                a['moving_time'],
                a.get('gear_id'),
                polyline
            ))

            # ✅ segments safe loop
            for s in full.get("segment_efforts", []):
                if not isinstance(s, dict):
                    continue

                seg = s.get('segment', {})
                if not seg:
                    continue

                c.execute("""
                INSERT INTO segments VALUES (?, ?, ?, ?)
                """, (
                    seg.get('id'),
                    s.get('name'),
                    s.get('distance'),
                    a['id']
                ))

        conn.commit()
        conn.close()

        page += 1
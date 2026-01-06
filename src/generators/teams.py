import random
from utils.uuid import generate_uuid
from datetime import datetime

TEAM_NAMES = {
    "Engineering": ["Platform", "Backend", "Infrastructure"],
    "Marketing": ["Growth", "Content", "SEO"],
    "Operations": ["Finance Ops", "HR Ops", "IT Ops"]
}

def generate_teams(conn, organization_id):
    cursor = conn.cursor()
    teams = []

    for dept, names in TEAM_NAMES.items():
        for name in names:
            team = {
                "team_id": generate_uuid(),
                "organization_id": organization_id,
                "name": f"{name} Team",
                "department": dept,
                "created_at": datetime.now()
            }

            cursor.execute("""
                INSERT INTO teams VALUES (?, ?, ?, ?, ?)
            """, tuple(team.values()))

            teams.append(team)

    conn.commit()
    return teams


def generate_team_memberships(conn, users, teams):
    cursor = conn.cursor()

    for user in users:
        team = random.choice(teams)
        user["team_ids"].append(team["team_id"])

        cursor.execute("""
            INSERT INTO team_memberships VALUES (?, ?, ?)
        """, (team["team_id"], user["user_id"], user["created_at"]))

    conn.commit()

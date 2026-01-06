import random
from datetime import timedelta
from utils.uuid import generate_uuid
from utils.dates import random_past_date

PROJECT_TYPES = ["Engineering", "Marketing", "Operations"]

def generate_projects(conn, organization_id, teams):
    cursor = conn.cursor()
    projects = []

    for team in teams:
        for _ in range(random.randint(5, 12)):
            start = random_past_date(6)
            end = start + timedelta(days=random.randint(30, 90)) if random.random() < 0.6 else None

            project = {
                "project_id": generate_uuid(),
                "organization_id": organization_id,
                "team_id": team["team_id"],
                "name": f"{team['department']} Project",
                "project_type": team["department"],
                "start_date": start,
                "end_date": end,
                "created_at": start
            }

            cursor.execute("""
                INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(project.values()))

            project["completion_probability"] = random.uniform(0.4, 0.85)
            projects.append(project)

    conn.commit()
    return projects

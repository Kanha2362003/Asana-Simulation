import random
from datetime import timedelta
from utils.uuid import generate_uuid
from utils.dates import random_past_datetime, random_future_date
from utils.text import generate_task_name, generate_task_description

def generate_tasks(conn, projects, sections, users, months_back=6):
    cursor = conn.cursor()
    tasks = []

    # Map project -> sections
    sections_by_project = {}
    for sec in sections:
        sections_by_project.setdefault(sec["project_id"], []).append(sec)

    # Map team -> users
    users_by_team = {}
    for user in users:
        for team_id in user["team_ids"]:
            users_by_team.setdefault(team_id, []).append(user)

    for project in projects:
        project_sections = sections_by_project.get(project["project_id"], [])
        team_users = users_by_team.get(project["team_id"], [])

        num_tasks = random.randint(80, 200)

        for _ in range(num_tasks):
            task_id = generate_uuid()
            created_at = random_past_datetime(months_back)

            is_subtask = random.random() < 0.28 and len(tasks) > 0
            parent_task_id = random.choice(tasks)["task_id"] if is_subtask else None

            if project_sections:

   
                weights = []
                for sec in project_sections:
                    if sec["name"] in ("To Do", "In Progress"):
                        weights.append(3)
                    elif sec["name"] == "Done":
                        weights.append(1)
                    else:
                        weights.append(2)

                section = random.choices(project_sections, weights=weights, k=1)[0]
            else:
                section = None

            assignee = (
                random.choice(team_users)["user_id"]
                if team_users and random.random() > 0.15
                else None
            )

            due_date = (
                random_future_date(created_at)
                if random.random() > 0.10
                else None
            )

            completed = random.random() < project["completion_probability"]
            completed_at = (
                created_at + timedelta(days=random.randint(1, 14))
                if completed
                else None
            )

            task = {
                "task_id": task_id,
                "project_id": project["project_id"],
                "section_id": section["section_id"] if section else None,
                "parent_task_id": parent_task_id,
                "name": generate_task_name(project["project_type"]),
                "description": generate_task_description(project["project_type"]),
                "assignee_id": assignee,
                "due_date": due_date,
                "completed": completed,
                "created_at": created_at,
                "completed_at": completed_at,
            }

            cursor.execute("""
                INSERT INTO tasks (
                    task_id, project_id, section_id, parent_task_id,
                    name, description, assignee_id, due_date,
                    completed, created_at, completed_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(task.values()))

            tasks.append(task)

    conn.commit()
    return tasks

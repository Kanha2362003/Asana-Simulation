import random
from utils.uuid import generate_uuid
from datetime import timedelta

def generate_comments(conn, tasks, users):
    cursor = conn.cursor()

    for task in tasks:
        if random.random() < 0.4:
            author = random.choice(users)
            cursor.execute("""
                INSERT INTO comments VALUES (?, ?, ?, ?, ?)
            """, (
                generate_uuid(),
                task["task_id"],
                author["user_id"],
                "Looks good, please proceed.",
                task["created_at"] + timedelta(days=1)
            ))

    conn.commit()

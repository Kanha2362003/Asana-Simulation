from utils.uuid import generate_uuid
import random

def generate_tags(conn):
    cursor = conn.cursor()
    tags = ["Urgent", "Backend", "Customer"]

    tag_objs = []
    for tag in tags:
        tag_id = generate_uuid()
        cursor.execute("""
            INSERT INTO tags VALUES (?, ?, ?)
        """, (tag_id, tag, "red"))
        tag_objs.append({"tag_id": tag_id})

    conn.commit()
    return tag_objs


def generate_task_tags(conn, tasks, tags):
    cursor = conn.cursor()

    for task in tasks:
        if random.random() < 0.4:
            tag = random.choice(tags)
            cursor.execute("""
                INSERT INTO task_tags VALUES (?, ?)
            """, (task["task_id"], tag["tag_id"]))

    conn.commit()

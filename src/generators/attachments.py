from utils.uuid import generate_uuid
import random
from datetime import timedelta

def generate_attachments(conn, tasks):
    cursor = conn.cursor()

    for task in tasks:
        if random.random() < 0.2:
            cursor.execute("""
                INSERT INTO attachments VALUES (?, ?, ?, ?, ?)
            """, (
                generate_uuid(),
                task["task_id"],
                "spec_document.pdf",
                "pdf",
                task["created_at"] + timedelta(days=2)
            ))

    conn.commit()

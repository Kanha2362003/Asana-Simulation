from utils.uuid import generate_uuid
from datetime import datetime

def generate_custom_fields(conn, organization_id):
    cursor = conn.cursor()

    fields = ["Priority", "Effort", "Story Points"]

    for field in fields:
        cursor.execute("""
            INSERT INTO custom_field_definitions VALUES (?, ?, ?, ?, ?)
        """, (
            generate_uuid(),
            organization_id,
            field,
            "text",
            datetime.now()
        ))

    conn.commit()

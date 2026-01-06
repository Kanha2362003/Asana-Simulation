from datetime import datetime
from utils.uuid import generate_uuid

def generate_organization(conn):
    cursor = conn.cursor()

    org_id = generate_uuid()
    cursor.execute("""
        INSERT INTO organizations (organization_id, name, domain, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        org_id,
        "Acme SaaS Technologies",
        "acme.com",
        datetime.now()
    ))

    conn.commit()
    return org_id

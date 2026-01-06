import random
from utils.uuid import generate_uuid
from utils.dates import random_past_datetime

FIRST_NAMES = ["Aarav", "Rohan", "Ananya", "Neha", "Kunal", "Isha"]
LAST_NAMES = ["Sharma", "Gupta", "Verma", "Singh", "Patel"]

ROLES = ["IC", "Manager", "Admin"]
DEPARTMENTS = ["Engineering", "Marketing", "Operations"]


def generate_users(conn, organization_id, num_users=7000):
    cursor = conn.cursor()
    users = []
    used_emails = set()

    for _ in range(num_users):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)

        # ---- UNIQUE EMAIL LOGIC (FIXED) ----
        base_email = f"{first.lower()}.{last.lower()}"
        email = f"{base_email}@acme.com"
        counter = 1

        while email in used_emails:
            email = f"{base_email}{counter}@acme.com"
            counter += 1

        used_emails.add(email)
        # -----------------------------------

        user = {
            "user_id": generate_uuid(),
            "organization_id": organization_id,
            "full_name": f"{first} {last}",
            "email": email,
            "role": random.choices(ROLES, weights=[75, 20, 5])[0],
            "department": random.choice(DEPARTMENTS),
            "created_at": random_past_datetime(12),
            "is_active": random.random() < 0.95,
            "team_ids": []
        }

        cursor.execute("""
            INSERT INTO users (
                user_id, organization_id, full_name, email,
                role, department, created_at, is_active
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user["user_id"],
            user["organization_id"],
            user["full_name"],
            user["email"],
            user["role"],
            user["department"],
            user["created_at"],
            user["is_active"]
        ))

        users.append(user)

    conn.commit()
    return users

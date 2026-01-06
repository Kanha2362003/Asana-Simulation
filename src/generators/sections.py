from utils.uuid import generate_uuid

SECTIONS = ["Backlog", "To Do", "In Progress", "Review", "Done"]

def generate_sections(conn, projects):
    cursor = conn.cursor()
    sections = []

    for project in projects:
        for i, name in enumerate(SECTIONS):
            section = {
                "section_id": generate_uuid(),
                "project_id": project["project_id"],
                "name": name,
                "position": i
            }

            cursor.execute("""
                INSERT INTO sections VALUES (?, ?, ?, ?)
            """, tuple(section.values()))

            sections.append(section)

    conn.commit()
    return sections

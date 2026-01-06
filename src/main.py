

from utils.db import get_connection, run_schema

from generators.organizations import generate_organization
from generators.users import generate_users
from generators.teams import generate_teams, generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.comments import generate_comments
from generators.custom_fields import generate_custom_fields
from generators.tags import generate_tags, generate_task_tags
from generators.attachments import generate_attachments


def main():
    conn = get_connection("output/asana_simulation.sqlite")
    run_schema(conn, "schema.sql")

    organization_id = generate_organization(conn)
    users = generate_users(conn, organization_id, num_users=7000)

    teams = generate_teams(conn, organization_id)
    generate_team_memberships(conn, users, teams)

    projects = generate_projects(conn, organization_id, teams)
    sections = generate_sections(conn, projects)

    tasks = generate_tasks(conn, projects, sections, users)
    generate_comments(conn, tasks, users)

    generate_custom_fields(conn, organization_id)

    tags = generate_tags(conn)
    generate_task_tags(conn, tasks, tags)

    generate_attachments(conn, tasks)

    conn.close()


if __name__ == "__main__":
    main()

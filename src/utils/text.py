import random

def generate_task_name(project_type):
    templates = {
        "Engineering": ["Fix API latency", "Refactor auth module", "Improve logging"],
        "Marketing": ["Launch email campaign", "Prepare social media creatives"],
        "Operations": ["Update SOP documentation", "Audit vendor invoices"]
    }
    return random.choice(templates.get(project_type, ["General task"]))

def generate_task_description(project_type):
    return f"Task related to {project_type.lower()} workflow."

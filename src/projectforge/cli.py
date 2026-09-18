import argparse
import random
from projectforge.generator import project_structure

PROJECT_NAMES = [
    "quick_structure",
    "task_structure",
    "web_structure",
    "web_project",
    "web_app",
    "app_structure",
    "web_structure",
    "project_structure"
    
]

parser = argparse.ArgumentParser(
    description = "Creating basic web dev structure quickly and conveniently"
)

parser.add_argument("project_name", nargs="?")

args = parser.parse_args()

response = ['yes', 'y', 'yep', 'yeah', 'ok', 'okay', 'sure']


if args.project_name:
    project_name = args.project_name
else:
    project_name = input("Enter a project name or press Enter for a suggestion: ").strip()

    if not project_name:
        project_name = random.choice(PROJECT_NAMES)

        preferred_name = input(f"Do you like {project_name}? (yes/no): ").lower().strip()

        if preferred_name not in response:
            while True:
                project_name = input("Enter your preferred name: ").strip()

                if project_name:
                    break

                print("Project name cannot be empty.")


project_structure(project_name)
print(f"🎉🎉 {project_name} has been added successfully!! 🎉🎉")


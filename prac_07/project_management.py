"""
Estimate: 1 hour
Actual: _____
"""
from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU = """
Menu:
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    projects = []
    projects = load_projects(projects, FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            try:
                filename = input("File to load: ")
                projects = load_projects(projects, filename)
            except OSError:
                print("Invalid filename")
        elif choice == "S":
            filename = input("File to save to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            project_name = input("Project name: ")
            update_project(projects, project_name)
        else:
            print("Invalid input, try again")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(projects, filename):
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, parts[2], parts[3], parts[4])
            projects.append(project)
            print(project)
    return projects


def save_projects(projects, filename):
    """project_file = open(filename, 'w')
    for project in projects:
        project_file.write(','.join(str(val) for val in project) + '\n')
    project_file.close()"""


def display_projects(projects):
    if projects:
        print("Incomplete projects: ")
        for project in projects:
            if str(project.completion_percentage) != str(100):
                print(project)
        print("Completed projects: ")
        for project in projects:
            if str(project.completion_percentage) == str(100):
                print(project)
    else:
        print("No projects")


def filter_projects(projects):
    date = input("Date: ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > date:
            print(project)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    while name != "":
        start_date = input("Start date(d/m/yyyy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
        new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(new_project)
        name = input("Name: ")


def update_project(projects, project_name):
    print()


main()

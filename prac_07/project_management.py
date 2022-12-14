"""
CP1404 Prac 7 - Project Management software using classes
Estimate: 2 hours
Actual: 2.5 hours
"""
from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
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
    """Takes user input for menu and runs relevant functions"""
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
            try:
                filename = input("File to save to: ")
                save_projects(projects, filename)
            except OSError:
                print("Invalid filename")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input, try again")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(projects, filename):
    """Extracts all data from a file specified by the user"""
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
    """Saves projects data into file specified by the user"""
    project_file = open(filename, 'w')
    print(HEADER, file=project_file)
    for project in projects:
        print(f"{project}", file=project_file)
    project_file.close()
    print(f"Data saved to: {filename}")


def display_projects(projects):
    """Displays all loaded projects and labels them as complete or incomplete"""
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
    """Displays all projects that began after user selected date"""
    date = input("Date: ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > date:
            print(project)


def add_project(projects):
    """Takes user input for project details and appends them to proejcts"""
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


def update_project(projects):
    """Allows user to change completion percent adn priority of existing project"""
    for i, project in enumerate(projects, 1):
        print(f"{i}: {project}")
    project_index = int(input("Project choice: "))
    for i, project in enumerate(projects, 1):
        if i == project_index:
            print(project)
            priority = int(input("New priority: "))
            if priority != "":
                project.priority = priority
            completion = int(input("New completion percentage: "))
            if completion != "":
                project.completion_percentage = completion


main()

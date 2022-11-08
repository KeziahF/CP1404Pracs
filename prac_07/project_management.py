"""
Estimate: 1 hour
Actual: _____
"""
from prac_07.project import Project
import datetime

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
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("File to load: ")
            projects = load_projects(projects, filename)
        elif choice == "S":
            filename = input("File to save to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_project
        elif choice == "U":
            update_project()
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
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
            print(project)
    return projects


def save_projects(projects, filename):
    print("saving projects")


def display_projects():
    print("displaying projects")


def filter_projects():
    print("filtering projects")


def add_project():
    print("adding projects")


def update_project():
    print("updating projects")


main()

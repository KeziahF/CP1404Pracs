"""
Estimate: 1 hour
Actual: _____
"""
from prac_07.project import Project

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
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
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


def load_projects():
    print("Loading projects")


def save_projects():
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

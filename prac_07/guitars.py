"""CP1404 Prac 6 - Using Guitar class to store and present data"""

from prac_06.guitar import Guitar


def main():
    """Takes user input and displays relevant guitar information"""
    guitars = []

    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost}")


main()
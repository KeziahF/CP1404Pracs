"""CP1404 Prac 6 - Using Guitar class to store and present data"""

from prac_07.guitar import Guitar


def main():
    """Takes user input and displays relevant guitar information"""
    guitars = []
    FILEPATH = 'guitars.csv'

    in_file = open(FILEPATH, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, " added.")
        name = input("Name: ")

    if guitars:
        #guitars.sort()
        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost}")

        number_of_guitars = 0
        guitar_file = open(FILEPATH, 'w')
        for i, guitar in enumerate(guitars, 1):
            number_of_guitars += 1
            guitar_file.write(str(guitar.name for val in guitar) + '\n')
        guitar_file.close()
        print(f"{number_of_guitars} guitars saved to guitars.csv")
        print("Have a nice day :)")

    else:
        print("No guitars")






main()

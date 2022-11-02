"""CP1404 Prac 6 - Testing functionality of Guitar class"""

from prac_06.guitar import Guitar


def main():
    """Compares expected class values with actual values"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 10 Got {other.get_age()}")
    print(f"{guitar.name} is_vintage - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == '__main__':
    main()

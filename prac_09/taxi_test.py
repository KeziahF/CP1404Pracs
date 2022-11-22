"""
CP1404 Prac 9
Taxi test - runs tests for taxi class
"""

from prac_09.taxi import Taxi


def main():
    """simulation of functionality for taxi class"""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")


main()

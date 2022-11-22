"""
CP1404 Prac 9
Unreliable car test - runs tests for unreliable car class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """simulation of functionality for taxi class"""
    car = UnreliableCar("Prius 1", 100, 70)
    car.drive(40)
    print(car)
    car.drive(100)
    print(car)


main()

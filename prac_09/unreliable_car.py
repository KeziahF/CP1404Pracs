"""
CP1404/CP5632 Practical
Unreliable car class, derived from Car
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f'{self.name}, fuel={self.fuel}, odometer={self._odometer}'

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_numer = randint(1, 100)
        if random_numer >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

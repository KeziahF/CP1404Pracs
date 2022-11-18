"""CP1404 Prac 6 - Guitar class"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
    
        """Initialises a guitar insstance"""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns string of guitar information"""
        return f'{self.name} ({self.year}) : ${self.cost:.2f}'

    def get_age(self):
        """Returns the age of the guitar compared to the CURRENT YEAR"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Compares guitar age to VINTAGE AGE and returns True if it is vintage"""
        return self.get_age() >= VINTAGE_AGE
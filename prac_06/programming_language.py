"""CP1404 Practical - programming language class."""

class ProgrammingLanguage:
    """Respresent a programming language"""

    def __init__(self, name='', typing='', reflection='', year=0):
        """Initialise parameters into fields"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return strign when programming language information printed"""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, first appeared in {self.year}"


    def is_dynamic(self):
        """Returns true if the programming language is dynamic"""
        return self.typing == "Dynamic"
from musician import Musician
from guitar import Guitar


class Band():
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def __str__(self):
        return f"{self.name} ({' '.join(str(member) for member in self.members)})"

    def play(self):
        members_instruments = []
        for member in self.members:
            if len(member.instruments) != 0:
                members_instruments.append(f"{member.name} is playing: {member.instruments[0]}")
            else:
                members_instruments.append(f"{member.name} needs an instrument!")
        return "\n".join(members_instruments)

    def add(self, band_member):
        self.members.append(band_member)

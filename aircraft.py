""" Lets rephrase the Aircraft class to have polymorphism and inheritance.
    Polymorphism: It means that the same function name can be used for different types. This makes programming more intuitive and easier.
    Inheritance: Here the base/parent class is passed as parameter to the child class"""


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, seat_letter = self.seating_plan()
        return len(rows) * len(seat_letter)


class AirbusA319(Aircraft):

    def model(self):
        return "AirbusA319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


"""from aircraft import *
a=AirbusA319("G-169")
a.num_seats()
132
a.seating_plan()
(range(1, 23), 'ABCDEF')
"""

class Boing777(Aircraft):

    def model(self):
        return "Boing777"

    def seating_plan(self):
        return range(1, 50), "ABCDEFGHJ"

"""b=Boing777("UK-231")
b.num_seats()
441
b.model()
'Boing777'
"""
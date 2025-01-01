# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noOfSides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    # def noOfSides(self):
    #     print("I have 3 sides")

    def hey(self):
        print("Hey")


class Pentagon(Polygon):
    # overriding abstract method
    def noOfSides(self):
        print("I have 5 sides")


# Driver code
R = Triangle()
R.noOfSides()
R.hey()


R = Pentagon()
R.noOfSides()

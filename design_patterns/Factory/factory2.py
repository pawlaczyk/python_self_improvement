#coding=utf-8

from enum import Enum
from math import *


class CoodinatesSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y): # PyTHON NIE MA PRYWATNYCH KONSTRUKTORÓW , w sumie to nie ma nic prywatnego
        """Damy użytkownikowi nowe Api które zapewnia tworzenie punktów z układu kartezjańskiego jak i polarnego
        Jeden dzieki konstruktowi dlaej mamy mozliwosc tradycyjnego tworzeniea obiektu współrzędnymi kartezjańskimi"""
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}; y: {self.y}'

    class PointFactory:
        def new_cartesian_point(self, x,y):
            """Statyczna metoda na tworzenie obiektw ze wsółrzędnych kartezajńskich"""
            return Point(x,y)

        def new_polar_point(self, rho, theta):
            """Metoda lepiej opisana - widać w jaki sposób inijalizujemy, nazwy zmiennych są też opisowe"""
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory() #teraz jest atrybutem klasy Point i singletonem


if __name__ == "__main__":
    p = Point(2,3)
    p2 = Point.factory.new_polar_point(1,2)
    p3 = Point.PointFactory().new_cartesian_point(1,2)
    print(p)
    print(p2)
    print(p3)


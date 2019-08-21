#coding=utf-8

from abc import ABC


class Shape(ABC):
    def __str__(self):
        print("")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        """metoda dostepne tylk odla obiektów klasy Cricle"""
        self.radius *= factor

    def __str__(self):
        return f'A circle of radus  {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    """dziedziczymy po Shape bo klasa ma działać zarówno z Circle jak i Square"""
    def __init__(self, shape, color):

        if isinstance(shape, ColoredShape):#obługa by nie używac tego samego dekoratora dwa razy
            raise Exception("Cannot apply the same decorator twice.")
        self.shape = shape #REFERENJCA do dekorowanego obiektu
        self.color = color

    def __str__(self):
        return f'{self.shape} has the color {self.color}' # {self.shape} zwraca tutaj  wynik z metody
        # Cricle.__str__  lub Square.__str__ zaleznie od tego jakiego typu jest przekazane shape


class TransparentShape(Shape):
    """dziedziczymy po Shape bo klasa ma działać zarówno z Circle jak i Square"""

    def __init__(self, shape, transparency):
        self.shape = shape #REFERENJCA do dekorowanego obiektu
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100.0}% transparency'


if __name__ == "__main__":
    # tworzenie okręgu
    circle = Circle(2)
    print(circle)

    # dodawanie funckjonalnosci koloru okręgowi bez jego modyfikacji jego klasy (Circle) samej w sobie - Simple Responsibility Pronciple
    red_circle = ColoredShape(circle, "red")
    # red_circle.resize(4) #AttributeError: 'ColoredShape' object has no attribute 'resize' #różnica międyz dziedziczeniem a REFERENCJĄ do obiektu
    print(red_circle)

    red_half_tranparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_tranparent_circle)

    #próba dwukrotnego uzycia tego samego dekoratora na obiekcie,gdize dekorator ma zaimplmentowany wyjątek na takie sytuacje
    # mixed_square = ColoredShape(ColoredShape(Square(3), 'red'), 'green') #eleancko zwróci wyjatek
    #Exception: Cannot apply the same decorator twice.


    # ale np taki układ już nie zwróci wyjatku
    nested_decorators_shape = TransparentShape(ColoredShape(TransparentShape(ColoredShape(Square(8),'red'), 0.5), "green"), 0.8)
    print(nested_decorators_shape) # to niestety bardzo cieżka do wychwycenia sytuacja

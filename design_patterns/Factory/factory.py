#coding=utf-8

class ShapeInterface:
    """Interfejs - Klasa abstrakcyjna"""
    def draw(self):
        pass


class Circle(ShapeInterface):
    """Konkretna subklasa - implmentacja"""
    def draw(self):
        """implementacja metody z interfejsu"""
        print("Circle.draw")


class Square(ShapeInterface):
    """Konkretna subklasa - implmentacja"""
    def draw(self):
        """implementacja metody z interfejsu"""
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == "circle":
            return Circle()
        if type == "square":
            return Square()
        assert 0, 'Could not find shape: ' + type


if __name__ == "__main__":
    factory = ShapeFactory()
    square = factory.getShape("square")
    square.draw()

    # triangle = factory.getShape("tirangle")
    # triangle.draw()

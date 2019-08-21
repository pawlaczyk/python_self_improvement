#coding=utf-8

# ------------- abstract shape classes -------------
# dwie rodziny bazowych interfejsow
class Shape2DInterface:
    """Interfejs dla rodziny figur 2D"""
    def draw(self):
        pass


class Shape3DInterface:
    """Interfejs dla rodziny figur 3D"""
    def draw(self):pass


# ------------- concrete shape classes -------------
class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")


class Square(Shape2DInterface):
    def draw(self):
        print("Shape.draw")


class Spehere(Shape3DInterface):
    def draw(self):
        print("Sphere.build")


class Cube(Shape3DInterface):
    def draw(self):
        print("Cube.build")


# ------------- Abstract shape factory -------------
class ShapeFactoryInterface:
    def getShape(sides): pass

# ------------- Concrete shape factories -------------
#FABRYKI ZWRACAJĄ OBIEKTY KTÓRE IMPLEMENTUJĄ TEN SAM INTERFEJS
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Bad 2D shape creation: shape not defined fo: " + sides + "sides"


class Shape3DFactory(ShapeFactoryInterface):
    """Nie tworzyć obiektów innych interfejsów - tutaj zgodnie z logika mozna by sie pokusic o utworzenie obiektow @d"""
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Spehere()
        if sides == 6:
            return Cube()
        assert 0, "Bad 3D shpe creation: shape not defined for: " + sides + "faces"


if __name__ == "__main__":
    factory2D = Shape2DFactory()
    factory2D.getShape(1)
    factory2D.getShape(1).draw()

    factory3D = Shape3DFactory()
    factory3D.getShape(1)
    factory3D.getShape(1).draw()

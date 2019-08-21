#coding=utf-8
"""
Separate the construction of a complex object from its representation so that the same construction process can create
different representations. This means we can use the same construction process to create different represenation.
For example building the different cars models.
So the pattern just allows us to have one class that undersands the recipe of the construction method and the different
classes have the responsibility of nowing what the parts are. And the we an put those together
"""

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %s" % self.__engine.horsepower)
        print("tire size: %d" % self.__wheels[0].size)


# --- Car parts ---
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def getCar(self)->Car:
        car = Car()

        #first goest the body
        body = self.__builder.getBody()
        car.setBody(body)

        #The engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4: #ale paskunda ta petla ojoj
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car #zwraca otowy samochow


class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


class JeepBuilder(BuilderInterface):
    """konkretna implementacja konkretnego modelu samochodu - Jeep tutaj"""

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22#konkretne wartosści dla konkretnego modelu samochodu
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400 #konkretne wartosści dla konkretnego modelu samochodu
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV" #konkretne wartosści dla konkretnego modelu samochodu
        return body


class NissanBuilder(BuilderInterface):
    """konkretna implementacja konkretnego modelu samochodu - Nissan tutaj"""

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16 #konkretne wartosści dla konkretnego modelu samochodu
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100 #konkretne wartosści dla konkretnego modelu samochodu
        return engine

    def getBody(self):
        body = Body()
        body.shape = "hatchback" #konkretne wartosści dla konkretnego modelu samochodu
        return body


if __name__ == "__main__":
    directorJeep = Director()
    directorJeep.setBuilder(JeepBuilder()) #ustawienie jako atrybutu dyrektora obiketu knkrentego Buildera - tutaj Jeep
    jeepCar = directorJeep.getCar()
    print(jeepCar.specification())

    directorNissan = Director()
    directorNissan.setBuilder(NissanBuilder()) #ustawienie jako atrybutu dyrektora obiketu knkrentego Buildera - tutaj Jeep
    nissanCar = directorNissan.getCar()
    print(nissanCar.specification())
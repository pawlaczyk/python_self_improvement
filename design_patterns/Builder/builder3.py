#coding=utf-8

"""
Builder z użyciem interfejsów - rozwiązania problemu naruszania zasady OPEN-CLOSED
Zgodne z zasadą open-closed - buildery można dziedziczyć w nieskończonośc, bo w idealnym świecie nigdy już nie trzeba
wracać do raz zaimplementowanych PersonBuilder czy PersonInfoBuilder - są one zamnkięte na modyfikację a jednocześnie
dodatkowe funckjonalności można  dodawac poprzez dziedziczenie już stworzonych builderów

Dziedziczenie pozwala na rozdzielenie builderów gdy te same w sobie stają się już zbyt skomplikowane
"""

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth}' +\
            f' works as {self.position}'

    @staticmethod
    def new(): #inicjalizacja buildera poprzez metodę statyczną
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        """Główny builder tylko buduje i zwraca obiekt"""
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder): #subbuilder głównego buildera
    def called(self, name):
        self.person.name = name
        return self #builder zwraca siebie co zapenia elastycznosć buildera


class PersonJobBuilder(PersonInfoBuilder): #subbuilder subbuildera
    def works_as_a(self, position):
        self.person.position = position
        return self #builder zwraca siebie co zapenia elastycznosć buildera


class PersonBirthDateBuilder(PersonJobBuilder): #subbuilder drugiego subbuildera (trzecie dziedziczenie)
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self #builder zwraca siebie co zapenia elastycznosć buildera





if __name__ == "__main__":
    pb = PersonBirthDateBuilder()
    me = pb\
            .called("Dmitri")\
            .works_as_a('Quant')\
            .born('1/1/1980')\
            .build()


    print(me)
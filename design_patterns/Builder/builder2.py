#coding=utf-8
"""
UWAGA - bezpośrednie naruszenie zasady OPEN-CLOSED ponieważą każdy subbuilder dziedziczący po glównym builderze trzeba dodac do głównego buildera
"""


class Person:
    def __init__(self):
        #brak argumentow inicjalzujacych - bedziemy budowac przez buildera
        # address information
        self.street_address = None
        self.postcode = None
        self.city = None

        #employment information
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}' +\
            f'Employed at {self.company_name} as a {self.position} earning {self.annual_income}'


class PersonBuilder: # facade
    def __init__(self, person = Person()): #sztuczka wymaga pustego initu, pustej osoby
        # sztuczka z person = Person() jako argument pozwala subbuilderom na pracowanie z obiektem który już skonstruowano
        #zamiast za każdym razem customizować coś gdy chcemy dodatkowej repliki
        self.person = person

    def build(self):
        # zwraca skonstruowany obiket po zakonczeniu procesu jego konstrukcji
        return self.person

    @property
    def works(self):
        # 3ładna sztuczna z propertisem
        return PersonJobBuilder(self.person) #żeby sztuczka zadziałą trzeba pracować na obiekcie już stworzonym

    @property
    def lives(self):
        # 3ładna sztuczna z propertisem
        return PersonAddressBuilder(self.person) #żeby sztuczka zadziałą trzeba pracować na obiekcie już stworzonym


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person): #nie tworzymy tutaj obiektu bo chcemy go przeazac i pracowac juz z istniejacym obiektem
        super().__init__(person) #używamy i modyfikujemy obiekt przekazany  z PersonBuilder i z powrotem go przekazujemy

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income= annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person): #nie tworzymy tutaj obiektu bo chcemy go przeazac i pracowac juz z istniejacym obiektem
        super().__init__(person) #używamy i modyfikujemy obiekt przekazany  z PersonBuilder i z powrotem go przekazujemy

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode= postcode
        return self

    def in_city(self, city):
        self.person.city= city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    person = pb\
        .lives.at("123 Londoan Road").in_city('London').with_postcode("SW123")\
        .works.at("Fabrikam").as_a("Operator").earning(123324)\
        .build()

    print(person)


class Animal:
    def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
        self.__birth_type = birth_type
        self.__appearance = appearance
        self.__blooded = blooded

    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, value):
        self.__birth_type = value

    @property
    def apperance(self):
        return self.__appearance

    @apperance.setter
    def apperance(self, value):
        self.__appearance = value

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, value):
        self.__blooded = value

    def __str__(self):
        return  "A {} is {} it is {} it is {}".format(
            type(self).__name__,
            self.birth_type,
            self.apperance,
            self.blooded
        )


class Mammal(Animal):
    def __init__(self, birth_type="born_alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurse_young=True):
        Animal.__init__(self, birth_type, appearance, blooded)
        self.__nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, value):
        self.__nurse_young = value

    def __str__(self):
        return super().__str__() + " and it has {} they nurse their young".format(self.nurse_young)


class Reptile(Animal):
    def __init__(self,
                 birth_type="bor in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):
        Animal.__init__(self, birth_type, appearance, blooded)



def main():
    animal1 = Animal("born alive")
    print(animal1.birth_type)
    print(animal1)

    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.birth_type)
    print(mammal1.apperance)
    print(mammal1.blooded)
    print(mammal1.nurse_young)

    reptile1 = Reptile()
    print(reptile1.birth_type)
    print(reptile1.apperance)
    print(reptile1.blooded)

main()
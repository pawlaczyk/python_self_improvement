#coding=utf-8
"""
Przykład dla automatu który robi kawę albo herbatę
"""

from abc import ABC


# ----------------------Hierarchy of different types
from enum import Enum, auto


class HotDrint(ABC):
    """abstrakcyjna"""
    def consume(self):
        pass


class Tea(HotDrint):
    def consume(self):
        print("This tea is delisous")


class Coffe(HotDrint):
    def consume(self):
        print("This coffe is delicious")


#-------------------------- Hierarchy of factories

class HotDrinkFactory(ABC):# klasę abstrakcyjnej fabryki można ywalić bo duck typing
    #jednak taka klasa abstrakcyjna jawnie mówi czego sie uzywa i jakie mamy API - czytelniejszy lepszy zwyczaj
    """The only reason why we have an abstract base class is to mandate a particular API to say that whenever
    you have an inherited that inherit there has to have a method called prepare which takes an amount.
    That's that's pretty much the only benefit."""
    #tutaj tak naprawde nie ma żadnej potrzeby tworzenia klasy abstrakcyjne fabryki
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount): #metoda produkująca obiekt
        """Oczywiscie metode mozna bardziej skastomizowac tworzac spefcyficzny obiekt herbaty"""
        print(f'Put in tea bug, boild water, ',
              f' pour {amount} ml. \nEnjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
# class CoffeeFactory(): Zadziała bo duck typing
    def prepare(self, amount): #metoda produkująca obiekt
        print(f'Grid some beans, boild water, ',
              f' pour {amount} ml. \nEnjoy!')
        return Coffe()


def make_drink_type(typeDrink):
# def make_drink_type(typeDrink): Zadziała bo duck typing
    if typeDrink == "tea":
        return TeaFactory().prepare(250)
    elif typeDrink == "coffe":
        return CoffeeFactory().prepare(50)
    else:
        None


class HotDrinkMachine:
    class AvailableDrink(Enum): #uzycie emuma jest niezgodne z open-closed bo jak dojdzie kolejny zestaw napojów to trzeba również tę klasę modyfikować
        COFFEE = auto()
        TEA = auto()

    factories = [] #w pytkhonie duck typing - lista jest dalej listą obiektów nie wazne w pythonie jakiego typu dlatego
    # bez klasy bazowej abstrakcyjen to wszystko zadziała
    # a np w Javie już nie bo jest silnie typowana
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            #inicjalizacja fabryk
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower() #name of actual drink
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)() #wiem że wszystkie fabryki nie pobieraja inicjalizujacych wartosci
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Pleae pick drink (0-{len(self.factories)-1}):')
        idx = int(s)
        s = input(f'Specify amount:')
        amount = int(s)
        #ponize zwracamy cos, wiec można do konsumowac
        return self.factories[idx][1].prepare(amount) #pierwszy to nazwa fabryki, drugi to instancja fabryki i na nim metode






if __name__ == "__main__":
    # entry = input('What kind of drink, would you like')
    # drink = make_drink_type(entry)
    # drink.consume()

    hdm =  HotDrinkMachine()
    hdm.make_drink()

"""
KACZE TYPOWANIE - NIE POTRZEBA KLASY ABSTRAKCYJNEJ FABRYKI W TYM JĘZYKU
Now one thing you once again notice and this is important is that there is really no need for the base

here.

So there is no need for the abstract ordering factory in fact if I commented out apart from these things

everything will continue to work.

So I can get rid of both of these and everything will continue to work as before there's absolutely

no problem in any of this because essentially Python uses duck typing so when we make a list here a

list of factories this list is not type to a hot drink factory so everything still continues to work.

However obviously in the kind of strong typing programming languages in literature you're going to see

the reference to an abstract base class for the factory is which is essential in other languages but

it's kind of optional in Python obviously it's a good idea because it then tells you what kind of API
"""
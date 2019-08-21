#coding=utf-8
"""
Przykład gdzie mamy grę multi-user
problem polega na tym, że mam wielu użytkownikow o tej samej nazwie typu John Smith, Sam Smith, John Doe etc.
a chcesz uniknąc przechowywania duzej ilosci danych w pamieci w szczególności gd są one do siebie podobne

"""

import string
import random


class User:
    def __init__(self, name):
        """ ładnie wyglądajaca ale NIEefektywana klasa"""
        self.name = name


class User2:
    strings = [] #statyczna zmienna

    def __init__(self, fullname):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x)
                      for x in fullname.split(' ')]

    def __str__(self):
        # wyciagamy indeksy przechowywane ze zmiennej statycznej self.strings dla każdego litery z self.names
        return ''.join([self.strings[x] for x in self.names])

def random_string():
    """emulacja nazw użytkowników"""
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for i in range(8)])


if __name__ == "__main__":
    users = []
    first_names = [random_string() for i in range(100)] #tutaj tylko 200 unikalnych stringów
    last_names = [random_string() for i in range(100)] #tutaj tylko 200 unikalnych stringów
    # biorac pod uwage że mamy tylko 200 unikatowych first_names i 200 unikatowych last_name powinniśmy zużyć pamieci tylko na
    # 200 segmentów pamieci na stringi =>  z pomocą przychodzi wzorzec flyweight

    for first in first_names: #produkt kartezjanski
        for last in last_names:
            users.append(f'{first} {last}')

    print(users[0])
#coding=utf-8

"""
Generatory
Python Generators 1: Functions that yield, suspend, and resume

https://www.youtube.com/watch?v=Ut0-_eMVakU
https://osf.io/sk7h6/ #pliki do kursu

Generator function is a function that can suspend and resume (wznawianie) so it's 
diferent from regular function that can return a value nd are then finished and 
in conrast generator function can can return or yield as it is called for generator
functions value and then pick up where it left off to yield another value, and another value, and another value ...

Generator function is a way to generate a list of elements on the fly 

"""
import time
from gameworld import Animal, draw_grid

def cats():
    """
    Funkcja trajektorii ruchu kotałka - zwraca listę
    
    """
    l = [] #bo inaczej konflik naz i rekurenkcja xD
    for i in range(2,8): # <2,7>
        l.append(Animal(row=i, col=i))
    return l

def cats_generator():
    """
    generator - zamiast zwracać całą liste kotków zwraca pojedynczo obiekt puszka
    Zwórić kotka, potem sie wznowi i zwróci kolejne kitku

    Nadal jakby zwracamy listę kotków, ale teraz robimy to w locie, za kazdym razem iteracji z każym działaniem pętli for

    """
    for i in range(2,8): # <2,7>
        print('cat', i)
        yield Animal(row=i, col=i)
    # zakończy się jak już zwróci wszystkie kotki 

def mouse_generator():
    """
    Tworzenie obiketu myszki tez przez generator
    """
    for i in range(7,1, -1): #do tyłu dekrementacja
        print('mice', i)
        yield Animal(row=7, col=i) #tylko w poziomie idzie


for cat, mouse in zip(cats_generator(), mouse_generator()): #zip() żeby latac po elementach z obu list wtej samej kolejnosci
    """
    aynchonicznie o działa - doczytać, bo od python3.6 to jest już ładnie wbudowane
    """
    # draw_grid(cat, mouse)
    # time.sleep(.4) #0,4 sekundy
    pass
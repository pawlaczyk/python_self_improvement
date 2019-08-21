#coding=utf-8

"""
Generatory
Python Generators 1: Functions that yield, suspend, and resume

https://www.youtube.com/watch?v=x3N3JmgjXxg&index=2&list=PLR-r0edywujfqG6GRRcB3iFxnUYo_UBC1https://osf.io/sk7h6/ #pliki do kursu

Przerobienie na komunikacje obustronną pomiedzy generatorem kotka a generatorem myszki
Tak, zeby aktywnie mysz mogła uniknąc kitka

"""
import time
from gameworld import Animal, draw_grid

def cats_generator():
    """
    generator - zamiast zwracać całą liste kotków zwraca pojedynczo obiekt puszka
    Zwórić kotka, potem sie wznowi i zwróci kolejne kitku

    Nadal jakby zwracamy listę kotków, ale teraz robimy to w locie, za kazdym razem iteracji z każym działaniem pętli for

    """
    for i in range(2,8): # <2,7>
        # print('cat', i)
        yield Animal(row=i, col=i)
    # zakończy się jak już zwróci wszystkie kotki 

def mouse_generator():
    """
    Tworzenie obiketu myszki tez przez generator
    """
    for i in range(7,1, -1): #do tyłu dekrementacja
        # print('mice', i)
        yield Animal(row=7, col=i) #tylko w poziomie idzie



icat = cats_generator()
imouse = mouse_generator()

# the first time you have to do that you always first have to send None into 
# the iterator objects to kick off the corresponding generator funtions 
# it's bit strange, but you always have to start with sendingnow, but later ou can actually send information and 
cat = icat.send(None)
mouse = imouse.send(None) #to samo co dla cat

"""
Niezbyt czyste, ale oznacza to wysyłanie wartosci None do iteratora po raz pierwszy 
what we're going to to is kick off the corresponding generator function until
 it reaches its first yield segment
co oznacza że cat_generato() zostanie uruchominy i zwróci pierwszy 
obiekt z i=2, a ten wynik zostanie przypisany do zmiennej `cat`
so by sending Null into `icat` we've essentially kicked off the cats generator
"""

while True:
    """
    reinplementacja petli for, ale w sposób bezpośredni, czytelniejszy
    """
    draw_grid(cat, mouse)
    time.sleep(.4)

    try:
        # Po wykonaniu ruchu znowu wywołujemy obiekt z generatora, zeby dotać kolejnego kitka i mysz
        cat = icat.send(None)
        mouse = imouse.send(None) #to samo co dla   cat 
        # Zastopowalło się, ale przez wyjatek StopIteration
    except StopIteration:
        """
        StopIteration niekoniecznie jest błedem, jest po prostu sposobem, 
        zeby python zasygnalizował, to że pętla for w generatorze sie skończyła 
            -informacje, że zużyliśmy generator
        """
        break



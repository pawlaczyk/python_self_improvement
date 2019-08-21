#coding=utf-8

"""
Generatory
Python Generators 1: Functions that yield, suspend, and resume

https://www.youtube.com/watch?v=x3N3JmgjXxg&index=2&list=PLR-r0edywujfqG6GRRcB3iFxnUYo_UBC1https://osf.io/sk7h6/ #pliki do kursu

Przerobienie na komunikacje obustronną pomiedzy generatorem kotka a generatorem myszki
Tak, zeby aktywnie mysz mogła uniknąc kitka


komuinikacja między generatorami nie jest trywialna, ale jest bardzo użyteczna / powerfull

"""
import time
import random
from gameworld import Animal, draw_grid, move

def cats_generator():
    """
    komunikacja z generatorem myszy

    """
    cat = Animal(row=2, col=2)
    while True: # infinite generator
        mouse = yield cat # we sending the cat and we're receiving the mouse
        #mouse becomes a return value of the yield statement
        #so yield is what generated gifts and return value of the yield mouse in this case is what I generator gets
        #generator is finished when the function itself is finished or when the StopIteration exception is raised explicitly

        #  zmiana trajektorii kotka
        if mouse.row > cat.row:
            cat = move(cat, row=1)
        if mouse.row > cat.row:
            cat = move(cat, row=1)
        
        if mouse.col > cat.col:
            cat = move(cat, col=1)
        elif mouse.col < cat.col:
            cat = move(cat, col=-1)


def mouse_generator():
    """
    Tworzenie obiketu myszki tez przez generator
    """
    mouse = Animal(row=7, col=7)
    while True: # infinite generator
        cat = yield mouse # we sending the mouse and we're receiving the cat
        
        #zakończenie gry kiedy mysz zostanie złapana przez kota
        if mouse.col == cat.col and mouse.row == cat.row:
            raise StopIteration() # normalny sposób na informaowanie, ze iterator się zużył
            # to samo przy użyciu `break` - bo zakończyłoby to pętle while 

        #  zmiana trajektorii kotka
        if mouse.row > cat.row:
            mouse = move(mouse, row=1)
        elif mouse.row < cat.row:
            mouse = move(mouse, row=-1)
        else: #kiedy kot i mysz sa na tym samym wierszu
            mouse = move(mouse, row=random.choice([-1, 1]))

        if mouse.col > cat.col:
            mouse = move(mouse, col=1)
        elif mouse.col < cat.col:
            mouse = move(mouse, col=-1)
        else: #kiedy kot i mysz sa na tej samej kolumnie
            mouse = move(mouse, col=random.choice([-1, 1]))

icat = cats_generator()
imouse = mouse_generator()

# the first time you have to do that you always first have to send None into 
# the iterator objects to kick off the corresponding generator funtions 
# it's bit strange, but you always have to start with sendingnow, but later ou can actually send information and 
"""
Wysyłamy None, nie można wysłać nic innego bo spwoduje to bład - jedyna opcja, zeby dostać pierwszy obiket generatora
"""
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
        # Tutaj komunikacja , żeby mysz wiedziała o kocie i kot o myszy 
        """
        Tutaj wysyłamy do generatorw informacje
        """
        cat = icat.send(mouse)
        mouse = imouse.send(cat) #to samo co dla   cat 
        # Zastopowalło się, ale przez wyjatek StopIteration
    except StopIteration:
        """
        StopIteration niekoniecznie jest błedem, jest po prostu sposobem, 
        zeby python zasygnalizował, to że pętla for w generatorze sie skończyła 
            -informacje, że zużyliśmy generator
        """
        #gdybyśmy używali pętli for to byłoby obsłużone automatycznie
        # but if we have this kind of while loop explicit while loop we also need to 
        # explicitl catch the stop iteration exception
        print("Tuuuuuuuuuuu")
        break

draw_grid(cat, mouse) #ostatnia klatka, gdzie kot złapał mysz


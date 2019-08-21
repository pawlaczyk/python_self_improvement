#coding=utf-8

"""
[Wyrażenia generatora]
Generator expressions in Python [Python comprehensions #4)
https://www.youtube.com/watch?v=V2FOlOW0bTs&index=4&list=PLR-r0edywujd8D-R2Kue1C_wYEK_4Ii71
https://osf.io/wshd5/

mosst abstract form of comprehension in Python that you can build any kind of comphrehension
    regular genererator yield, and yield with returned value and communicate with outside world

generator can yield multiple return values it is essentialy like a list, because it can return multiple things 

generot function is inviting a so called iterable object it is something that has a collection of multiple things by
    virtue of the fact that it can have multiple return value

Generator exression is similar to generator function but it has a different kind of syntax 
intermidiate list comprehension and generator function

Ważna cecha generatora [!]
    moze być nieskończony !
    becauese the generator expression evaluates elemenst as you go along one element at a 
    time whereas all the other comprehensions lists set and dict comprehensions are evaluated completly when 
    theye are defined and becaues this reason a generator expression are more flexible tha all the other 
    comprehensions and you can do everything that you can do with the list set, or a dict comprehension also
    with the generator expression but in many cases a generator expression will just make things a little bit 
    more complicated than is necessary and you're better of using a list comprehension or something similar

"""

#  3 bedziemy generowac nieskończony generator lisczb 
import itertools

def is_prime(i):
    # [!] This is a generator expession [!]
    return all(i % j for j in range(2, i)) #okrągłe nawiasy

def is_fibbonchi(i):
    history = 0,1
    while sum(history) < i:
        history = history[1], sum(history)
    return sum(history) == i


def print_first(g, n=5):
    for i, _ in zip(g, range(n)):
        print(i)

# 1. With a generator function
def primofibo():
    """
    Traditional generator function
    """
    for i in itertools.count(): # coś jak pętla nieskończona
        if is_prime(i) and is_fibbonchi(i):
            yield i

# print_first(primofibo()) # obiekt z funkcji generatora
# print_first(primofibo(), n=10) # obiekt z funkcji generatora
"""
Jak to działa?
 - primofibo() wywołujemy funkcję generatora, która tworzy obiket iterowalny, po którym mozemy iterować, 
    będzie przekazany jako pierwszy parametr jako `g` w funkcji `print_first(g, n=5)
    potem przechodzimy pętla po tym za pomocą zip() z range(n) , żeby mieć pewność że działanie się zakończy (inczaej nieskończonośc) bo genrator nieskońzczony


"""

# 2. With generator expression
# primofibo = (i for i in itertools.count() if is_prime(i) and is_fibbonchi(i))
#gdyby to zrobic za pomocą list comprehension to natychmiast zostałyby utworzone wszystkie elemnety
"""
Indicate that it is a generator expression with these parentheses () waiting python will 
not immediately start evaluating this entire expession rather what it will do is domething that is called 
[lazy evaluation] it will generate new `i` whenever we ask for it 

różnica miedzy funkcją generatora jest taka, że przy wywołaniu 
    print_first(primofibo()) # obiekt z funkcji generatora trzeba jawnie podac obiekt generatora
    W wyrażeniu, po prostu wrzuacamy do printa wyrażenie generatora

so every time that we get the new elemnt from the generator expression  that's when the general 
    expression generator expression start to work
"""

############## List comprehension vs generator expression #################
"""
list comprehension which would start to do all the work as soon as we define the 
    list comprehension because as soon as we define the list comprehension that's when the 
    list is being generated so that is very different from generating beetwen a generetaor expression and the list comprehension
    the fact that the generator expression evaluates as we go along [lazy evaluaton] 
    whereas a list comrehension evaluates everything at once

"""


# print(primofibo) #tutaj wypisze wszystkie lementy bo o to poprosiliśmy
"""
1
2
3
5
13
1
2
3
5
13
89
233
1597
28657 
Po tych wartośc komp mieli aż słychać chłodzenie xD
"""

primofibo = ( i for i in range(100) if is_fibbonchi(i) and is_prime(i))
print(list(primofibo)) 
"""
python will take this generator expression evaluate it and turn into a 
list but like this and it is a list comprehension there is no semantic difference between 
this what I've typed here ends up typing it as a list comprehension right away

The list comprehension is essentialy a special case you could say or a generator expression 
to samo dla set(primofibot)
"""
primofibo = ( i for i in range(200) if is_fibbonchi(i) and is_prime(i))
print(set(primofibo)) # to samo jak dla list składanych - otrzymujemy od razu wszystkie wartośći
"""
so the set would take this generator expression evaluated it from start to finish 
and turn the result into is set because it will as soon as I call it turn it 
into a set or a list the entire contents of the generator expression will be evaluated and for that rang
for that reason i had to use fix range not infite itertool.count() range 
    primofibo_infinite = ( i for i in itertools.count() if is_fibbonchi(i) and is_prime(i))
    to ^ jest synaktycznie poprawne i niekoniecznie da błąd, ale po prostu się nie da wykonac, bo nieskońzoność [infinite evaluation]
    set(primofibo_infinite) python zacznie tworzyć zbiór nieskończonej ilosci elementów; co jest niemożliwe
"""


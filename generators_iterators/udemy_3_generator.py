#coding=utf-8
"""
Python Generator Expressions
zwraca anonimą funkję generatora, która nie ma w sobie słowa kluczowego `yield`

#Syntax Wyrażenie generatora:  # podobne do list comprehension
    Y = ([Expression]) # żeby dostać listę wymagane @Return: [1, 4, 9, 16, 25]
    Y = (Expression) # zwróci obiekt generatora; @Return: <generator object <genexpr> at 0x00000215D5711930>
    zwraca jeden elemntw jednym czasie

https://www.udemy.com/learn-advanced-python-programming/learn/v4/t/lecture/11821980?start=0

"""

y = [1,2,3,4,5]

print([x**2 for x in y]) # [1, 4, 9, 16, 25]

print((x**2 for x in y)) # <generator object <genexpr> at 0x00000215D5711930>

print((x**2 for x in y).__next__()) # Zwróci `1` - pierwszy element z generatora
# bo yield keyword returns only one elemnt at the time

generator = (x**3 for x in y)
for itr in generator:
    # po iteratorach można jak po listach iterowac, bo pętla for wykorzystuje metode __next__()
    print(itr) # ladnie wypisuje wszystkie elemnty :)
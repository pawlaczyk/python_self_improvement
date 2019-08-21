#coding=utf-8

"""
Python Tutorial - 22. Generators
https://www.youtube.com/watch?v=lJUZc3OhU7A&list=PLeo1K3hjS3usILfyvQlvUBokXkHPSve6S&index=24

Generator:
    - is a simply way of creating iterator

    - słowo kluczowe `yield` jest podobne do `return`, ale kiedy używa się retrurn to 
        funkcja zwraca dane i niszczy wszystkie swoje lokalne zmienne
    
    - przydatne gdy mamy listy wielkich danych i nie chcemy zwracac ich od razu za jednym zamachem
         gdy np. zajmują od groma pamięci
         [benefit of saving memory]
         [getting a quick processing]
"""

def remote_control_next():
    # funkcja działajaca jak pilot do TV - zwraca kolejny kanał
    # generator sam w sobie zapamietuje co ostatnio zwrócił :)
    yield "cnn"
    yield "espn"
    yield "HBO"

itr = remote_control_next()
print(itr) # <generator object remote_control_next at 0x00000297B6B91930>
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# Traceback (most recent call last):
#   File "generators_1.py", line 26, in <module>
#     print(next(itr))
# StopIteration

# for c in remote_control_next():
    # pętla for działa na generatorach
    # funckja zwraca generator and generator has an ability to be compliant with the for loop
    # so for loop can iterate throught over each of these values
    # print(c)


"""
Benefits of using generator over class based iterator,
1) You don't need to define iter() and next() method #krótszy kod
2) You don't need to raise StopIteration exception # generator sam to ogarnia zxe elemnty sie skonczyly

"""
def fib():
    #Fibonachi za pomocą generatora
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b # to sie wykonuje po zwroceniu wartosci yield; ale wyglada jak przed bo przed zwroceniem nastepnego elemntu ta linia sie wykonuje

for f in fib():
    if f > 100:
        break
    print(f)
#coding=utf-8

"""
PYTHON FUNCIONAL DECORATOR
Implementacja dekoratora wewnątrz Pythona jest bardzo specyficzna - nie jest to ten sam dekorator który znajdujemy w ksiażkach o OOP
czy taki, który implmenetuje się w javie
"""

import time
#przykład operacji które zajmują jakiś dłuższy czas
#założmy że chcemy znać czas - pomieżyć czas operacji jaki się wykonuje

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int((end-start)*1000)}ms')
        return result
    return wrapper



@time_it #python decorator
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123 #nie trzeba nic zwraćać, ale to po prostu dobra ilustracja


if __name__ == "__main__":
    #some_op()
    time_it(some_op)() #obiekt funkcji jako argument i wywołujemy tą wewnętrzną funckje wrapper()
    # some_op() #ten sam wynik co wyżej
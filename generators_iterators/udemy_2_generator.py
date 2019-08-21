#codig=utf-8
"""
Udemy Advanced python - [przykłady]
Generatory 2
https://www.udemy.com/learn-advanced-python-programming/learn/v4/t/lecture/11821976?start=0


Generator jest prostym sposobem tworzenia iteratorów
Generator is a simple way of creating iterator
generator jest funkcją która zwraca obiekt będący iteratorem, a ten iterator może być czytany i czytany
funkcja ze słowem kluczoywm `yield` automatycznie staje sie generatorem - jedyny wymóg na stworzenie generatora
generator moze mieć nawet więcj niż jesd yield; ale jeden jest wymagany (yield)

"""
#generator odwracający stringa
def reverse(word):
    length = len(word)

    for i in range(length -1, -1, -1): # iterowanie do tyłu
        yield word[i]
        # jeśli użyć return to zwróci tylko "n" ostatnią literę
    

for char in reverse("UmairKhan"):
    print(char)


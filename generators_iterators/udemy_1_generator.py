#coding=utf-8

"""
Advanced Python z Udemy
https://www.udemy.com/learn-advanced-python-programming/learn/v4/t/lecture/11821970?start=0


A generator is actually a materrer or a function with the difference that the normal function have a 
redone statement there as a funtion that has a statement insetead of return statement is called

generators are used to create troubles with a different style not similar to follow type iterators
generators are actually simple function which work done and travel a set of items one at a time

#Iterables and Yield
when you create a list you can read its items one by oneyou can only see one item at the time 
with one operation outputting one output only

"""
import time

# Przykład ze zwykłą funkcją, zwracajacą wartośc przez return
def call_received_function(received):
    """
    Funkcja która dodaje do `a` jeśli odpowiedź od użytkownika na pytanie `Did you received a call` jest `yes`

    """
    a = 0
    while True:
        if received == 'yes':
            a = a+1
            return a
        else:
            return a


def function_without_saving_state():
    """
    Zawsze zwróci 1, bo a jest zmienną lokalną i nie pamięta poprzedniego stanu
    Did you received a call or not? : yes
    TOTAL:  1
    Did you received a call or not? : yes
    TOTAL:  1
    Did you received a call or not? : yes
    TOTAL:  1
    Did you received a call or not? : yes
    TOTAL:  1
    Did you received a call or not? : yes
    TOTAL:  1
    Did you received a call or not? :

    """
    stoppage_time = time.time() + 5 * 60
    while time.time() < stoppage_time: # while uzależniony od czasu
        received = input("Did you received a call or not? : ")
        total = call_received_function(received)
        print("TOTAL: ", total)

# function_without_saving_state() # użycie zwykłej funckji


############################### RETURN vs YIELD ############################
# `return` statement
def x():
    """
    próba uzycia zwykłej funkcji jako generatora

    """
    return 'a'
    return 'b'
    return 'c'

def normal_function_return():
    """
    Zawsze wyprintuje `a` bo po pierwszym return funkcja zwraca wartosć 
    i niszczy swoje lokalne zmienne i stan

    """
    y = x()
    for i in range(3):
        print(y) # `a`

# normal_function_return() # normalna funkcja

#############################################################
# `yield` statement
def x_generator():
    """
    prosty generator
    Zwróci po kolei `a`, `b`, `c`
    
    """
    yield 'a' # przy drugiej iteracji pamieta, ze to już było zwrócone
    yield 'b' # zwróci przy drugiej iteracji
    yield 'c' # zwróci przy trzeciej iteracji

def generator_function_return():
    """
    Trzeba uzyć wbudowanej funkcji __next__(), która jest zawsze używana w funkcjach generatorów
    ładnie wyprintuje elemnty jak trzeba
    `a`
    `b`
    `c`

    The `yield` statement is used to restore the executioon from where it was last endend
    And it means for the most part the mission execution was ended
    """
    y = x()
    for i in range(3):
        print(y.__next__()) # iterowanie po elementach generatora

# generator_function_return() # generaotr

######################## Generator - zapamietywanie stanu ############################
def call_received_generator2(received=None): #we nedd to this received=None argument is forced 
    """
    Funkcja do zliczania połaczen za pomoca generatora, który 
    [!] UWAGA [!]
         bez przypisania yield do zmiennej received generator nie ważne od odpowiedzi zwraca  `a` == 0 :<
    
    """
    a = 0 
    while True:
        if received == 'yes':
            a += 1
            yield a #received zapamietuje stan
        else:
             yield a # bez inktrementacji, bo odpowiedź nie była `yes`



def call_received_generator(received=None): #we nedd to this received=None no argument is forced 
    """
    Funkcja do zliczania połaczen za pomoca generatora pamietajacego stan
    
    """
    a = 0 
    while True:
        if received == 'yes':
            a += 1
            received = yield a #received zapamietuje stan
        else:
            received = yield a # bez inktrementacji, bo odpowiedź nie była `yes`


# rec = call_received_generator2() #tutaj do generatora leci None; tutaj bez przypisania yield do zmiennej zaawsze zwróci 0 :<
rec = call_received_generator() #tutaj do generatora leci None

x = rec.__next__()
# print(x)

stoppage_time = time.time() + 5 * 60

while time.time() < stoppage_time:
    """
    Będzie się tak długo wykonywać, aż warunek czasu zostanie zerwany
    Uzywajac generatora ładnie zapamiętujemy poprzednie czasy

    Do you received a call or not?: yes
    1
    Do you received a call or not?: yes
    2
    Do you received a call or not?: yes
    3
    Do you received a call or not?: no
    3
    Do you received a call or not?: no
    3
    Do you received a call or not?: yes
    4
    Do you received a call or not?: esr
    4
    Do you received a call or not?: ser
    4
    Do you received a call or not?: yes
    5
    Do you received a call or not?: yes
    6
    Do you received a call or not?: yes
    7
    Do you received a call or not?: yse
    7
    Do you received a call or not?: yes
    8
    Do you received a call or not?: yes
    9
    Do you received a call or not?: 435
    9
    Do you received a call or not?: yes
    10

    """
    ans = input('Do you received a call or not?: ')
    print(str(rec.send(ans))) # przesylanie wartosci do generatora jako argument
    # dlatego w generatorze jest poprzedny received=None bo inaczej się wywali na ryjek




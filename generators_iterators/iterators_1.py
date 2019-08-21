#coding=utf-8
"""
https://www.youtube.com/watch?v=Fc1fLEk_Kr0

Debugowanie w Visaul studio Code F5
przechodzenie kolejno jest F10
breakpointy myszką po lewej, breakpointy mają fajne opcje np. log Message - nie trzeba biednie printowac :)
a wiadomosci z debuggera sa w konsoli debuggera na dole
Po lewej sa zmienne

"""
#użycie petli for do iterowania po elementach - standardowe użycie
# chodzenie element po elemencie jest nazywane iterowaniem 
# [iterating trought a loop]
# pętla używa wbudowanej funckji iter() __iter__
a = ["hey", "bro", "you'r", "awesome"]
# for i in a:
#     print(i)

# print(dir(a))

# itr = iter(a)
# print(itr) # <list_iterator object at 0x000001F68B7EEAC8>
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(iter)) #StopIeration Exception

# Przykłady iteratorów
# wszystkie te przykłady używają itertowów
# for element in [1,2,3]:
#     print(element)

# for element in (1,2,3): # tupla
#     print(element)

# for key in {'one' : 1, "two": 2}: # iterowanie po słowniku
#     print(key)

# for char in "123": # iterowanie po stringu
#     print(char)

# for line in open("myfile.txt"): # iterowanie po pliku
#     print(line)


# klasa iteratora - pilot do przełączanie kanałó
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "cnn", "abc", "espn"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1 # -1 +1 ==0 - zwroci pierwszy element za pierwszym razem
        print(self.index)
        if self.index == len(self.channels):
            StopIteration
        else:
            return self.channels[self.index]


r = RemoteControl()
itr = iter(r)
# print(itr) #<__main__.RemoteControl object at 0x0000024CE323EB38>ń
# print(dir(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) #StopIterator

# for i in r: #tu sie bedzie wychrzanaic, bo itertor się już "zużył"
#     print("i: ", i)
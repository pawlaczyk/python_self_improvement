#coding=utf-8
"""
https://www.youtube.com/watch?v=BC77x_GLmxo&list=PL1A2CSdiySGLPTXm0cTxlGYbReGqTcGRA&index=5

#Iterators
    - Used to loop through the items of container.
    - You will have used them before! 
        for element in [1,2,3]
    - Python uses the __iter__() method to return an iterator object of the class.
    - The iterato object then uses the __next__() method to get the next item.
    - The for loops stop when the StopIteration Exception is raised

"""

# #przykład iteratora
# s = 'abc'
# it = iter(s)
# print(next(it)) # a
# print(next(it)) # b
# print(next(it)) # c
# print(next(it)) # StopIteration exception
# """
# Traceback (most recent call last):
#   File "iterators_and_generators.py", line 21, in <module>
#     print(next(it)) # StopIteration exception
# StopIteration
# """


#reverse.py
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def main_iterator(): 
    rev = Reverse('Drapsicle')
    for char in rev:
        print(char)


"""
# Generators
    - Another way of creating iterators
    - Uses a function rather than a separate class
    - [!] Generates the background code for the next() and iter() methods 
        #dlatego sa szybkiec
    - Uses a special statement called `yield` 
        which saves the state of the generator and set 
        a resume point for whent next() is called again
    - Generator Expression are a unique feature that python uses
    - Allows for iteration to be handled in a single line expression
    - Uncommonly used by a lot of programmers

"""
def reverse_generator(data):
    # od ostatniego elementu do pierwsze co -1 (po prostu cofamy się w liście)
    for index in range(len(data) -1, -1, -1): 
        yield data[index]


def main_generator():
    rev = reverse_generator('Drapsicle') #generator za pomocą funkcji
    for char in rev:
        print(char)

    #za pomoca wyrażenia generatora
    data = 'Drapsicle'
    print(list(data[i] for i in range(len(data)-1 , -1, -1))) 


if __name__ == "__main__":
    # main_iterator() #wypisze litery w slowie od tylu
    main_generator()


# ------------------------//Challenge//------------------

# Try writing your own iterator class that allows you to specify the lengths of steps the iterator makes.
# eg.
#  when you call you step iterator class you specify the steps.

# string = Steps('Drapsicle', 2)
#     for char in rev:
#         print(char)

# which outputs
# D,a,s,c,e

# Then try writing a generator that does the same thing!

# Hint: Learn how the range() function works!.

# (I would love to see your finished program! 
# stick it on http://pastebin.com/ and send me the link via youtube inbox!)

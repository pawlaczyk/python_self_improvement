#coding=utf-8

"""
Why generators?

https://www.udemy.com/learn-advanced-python-programming/learn/v4/t/lecture/11821984?start=0

Advantages of generator:
    - easy to implement; utworzenie generatora jest raczej zmianą symboli, niż tworzeniem rozbudowanej klasy
    - memory efficient: a normale function returns a sequence in memory before rejoing the result. 
        this is overkill if the number of items in the sequence is really very large 
        generator implementation of such sequence is memory friendly and is crappes since it's only 
        produce one item at one time and saves a lot of memory
        The target at one stage of using a generator function is that it shoul present in infinite cheap generators
        Generators are excelent medium throught present an infinite stream of data - infinite stream of data cannot be stored in memory.
        And since Android releases only one item at a time it can represent infinite stream all data.
    - the purpouse of pipelining in generators explained by plannig engine generators.
        Suppose that you want to find the price of total crosstrees astall in 5 years as you need to maintain a long flight for all items that you
        keep in your store the log file will have a columnt that keeps track of all the number of grocery items that are stored in each are
        and you will want to sum it up and done the total define the total grocery stores sold in five years assume tha everything is in strings
        and numers that are not available aremarked as in generator implementation
        What pipelined this entire structure and it will be much moe efficient and easy to treat and yes a lot cooler and it will 
        not only reduce the time not only to reduce the memory but it will also be easy to look at and easy to read.


"""

######################## Zapis itertaor vs Zapis generatora ######################## 
#porówanie generatora i klasy iteratora
class Power:
    """
    Klasa iteratora, działa jak generator ale jest trudniejsza w zapisie
    - wymaganae metody to __iter__() i __next__()
    """
    def __init__(self, _max=0):
        self.max = _max

    def __iter__(self, n):
        """
        Każdy iterator ma funkcję __iter__()
        """
        self.n = n
        return self # iter zwraca siebie - obiekt iteratora

    def __next__(self):
        """
        Każdy iterator ma funkcję __next__()
        """
        if self.n > self.max:
            raise StopIteration # sygnalizowanie, że iterota się `zużył`
        
        result =  2 ** self.n
        self.n += 1
        return result

x = Power(5)
x.__iter__(2) #żeby zwrcił siebie 
print(x.__next__()) # `1` dla self.n = 0; 4 dla self.n = 2; dla n=1 zwraca blad

    
# generator function
def gen(max=0):
    a = 0
    while a < max:
        yield 2 ** a
        a += 1

print(gen(5))
print(gen(5).__next__())



#################### 
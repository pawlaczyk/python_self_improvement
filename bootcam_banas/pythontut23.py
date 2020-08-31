samp_str = iter("Sample")
print("Char: :", next(samp_str))
print("Char: :", next(samp_str))

class Alphabet:
    def __init__(self):
        self.letters = "abcdefghijklmnoprstuvwx"
        self.index = -1

    def __iter__(self):
        #metoda dla iteratora
        return self

    def __next__(self):
        if self.index >= len(self.letters) -1:
            raise StopIteration
        self.index +=1
        return self.letters[self.index]


alphabet = Alphabet()
for letter in alphabet:
    print(letter)

derek = {"f_name": "Derek", "l_name": "Banas"}
for key in derek:
    print(key, derek[key])

##########################
# Fibb class jako iterator
class Fib:
    def __init__(self):
        self.last = None
        self.last_last = None
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index == 0:
            self.last_last = 0
            self.last = 0
        elif self.index == 1:
            self.last_last = 0
            self.last = 1
        else:
            tmp = self.last + self.last_last
            self.last_last = self.last
            self.last = tmp

        return self.last

fib = Fib()
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())


class FibGenerator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num


fib_seq = FibGenerator()
for i in range(10):
    print("fib: ", next(fib_seq))
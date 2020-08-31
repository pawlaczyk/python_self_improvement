class Sum:
    @staticmethod
    def get_sum(*args):
        _sum = 0
        for i in args:
            _sum += i
        return _sum


class Dog:
    # static variables; shared by every object this class
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1 #dostep do statycznej wartosic

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


# import sum
# print("Sum: ",sum.get_sum(1,2,3,4,5))

from sum import get_sum
print("Sum: ", get_sum(1,2,3,4,5))


def main():
    print("Sum: ", Sum.get_sum(1,2,3,4,5,6,7))
    spot = Dog("Spot")
    spot.get_num_of_dogs()
    doug = Dog("Doug")
    Dog.get_num_of_dogs()

main()
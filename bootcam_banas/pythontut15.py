# class Dog:
#     def __init__(self, name="", height=0, weight=0):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def run(self):
#         print("{} the dog runs".format(self.name))
#
#     def eat(self):
#         print("{} the dog eats".format(self.name))
#
#     def bark(self):
#         print("{} the dog barks".format(self.name))
#
#
# def main():
#     spot = Dog("Spot", 66, 26)
#     spot.bark()
#
# main()

class Square:
    def __init__(self, height="0", width="0"):
        self.height123 = height
        self.width2131 = width

    @property
    def height(self):
        print("Retriving the information")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Pleas only enter numbers for height")

    @property
    def width(self):
        print("Retriving the information")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Pleas only enter numbers for width")

    def get_are(self):
        return int(self.__width) * int(self.__height)


def main():
    square = Square()
    height = input("Enter height")
    width = input("Enter width")
    square.height = height
    square.width = width
    print("height: ", square.height)
    print("width: ", square.width)
    print("The area is: ", square.get_are())

main()
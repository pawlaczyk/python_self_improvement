# def mult_divide(num_1, num_2):
#     return (num_1 * num_2), (num_1 / num_2)
#
# mult, divide = mult_divide(5, 4)
# print("mult: ", mult)
# print("divide: ", divide)


# def is_prime(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return False
#     return True
#
#
# def get_primes(max_number):
#     list_of_primes = []
#     for num_1 in range(2, max_number):
#         if is_prime(num_1):
#             list_of_primes.append(num_1)
#     return list_of_primes
#
#
# max_num_to_check = int(input("Search for Primes up to : "))
# list_of_primes = get_primes(max_num_to_check)
# for prime in list_of_primes:
#     print(prime)

# def sum_all(*args):
#     sum_1 = 0
#     for i in args:
#         sum_1 += i
#     return sum_1
#
# print("Suma: ", sum_all(1,2,3,4,5))

import math


def get_ares(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


def rectangle_area():
    length = float(input("Enter the length"))
    width = float(input("Enter the width"))
    area = length * width
    print("Th are of the rectangle is: ", area)


def circle_area():
    radius = float(input("Enter the radius: "))
    area = math.pi * (math.pow(radius, 2))
    print("The are of the circle is: {:.2f}".format(area))


def main():
    shape_type = input("Get area for what shape: ")
    get_ares(shape_type)

main()
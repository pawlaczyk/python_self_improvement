"""
num_1, num_2 = input("Enter 2 Numbers: ").split()
num_1 = int(num_1)
num_2 = int(num_2)
sum_1 = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2

print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, difference))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))
"""

"""
miles = int(input("Enter miles value: "))
kilometers = miles * 1.60934
print("{} miles equals km".format(miles, kilometers))
"""

import math

print("ceil(4.4) = ", math.ceil(4.4))
print("ceil(4.4) = ", math.floor(4.4))
print("fabs(4.4) = ", math.fabs(4.4))

# factorial
print("factorila(4) = ", math.factorial(4))

# reminder of division
print("fmod(5,4) = ", math.fmod(5,4))

# receive a float and return an int
print("trunx(4.2) = ", math.trunc(4.2))

# x ^ y
print("pow(2,2)", math.pow(2,2))

#return the square root
print("sqrt(4) = ", math.sqrt(4))

#special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# define the base and 10^3 =1000
print("log(1000, 10) = ", math.log(1000, 10))

# you can also use 10 like this
print("log10(1000)= ", math.log10(1000))
print("Natuarl logarithm base e: ", math.log(10))

# trigonometry functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh, atanh, sinh, cosh, tanh
print("sin(0) ", math.sin(0))

#convert radias to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))


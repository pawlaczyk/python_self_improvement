# while True:
#     try:
#         number = int(input("Please enter the number: "))
#         break
#     except ValueError:
#         print("You didn't enter the number")
#     except:
#         print("An unknown error occured")
#
# print("Than you for entering number")

# secret = 7
# number = None
# while True:
#     try:
#         number = int(input("Enter the number: "))
#     except ValueError:
#         print("You didnt enter the number")
#         continue
#
#     if number == secret:
#         print("You guessed number")
#         break
#     else:
#         print("try again")

# from decimal import Decimal as D
#
# sum = D(0)
# sum +=D("0.01")
# sum +=D("0.01")
# sum +=D("0.01")
# sum -=D("0.03")
# print("Sum= ", sum)

from decimal import *
sum_1 = Decimal(0)
sum_1 += Decimal("0.0111111111111111") # 16 cyfr po przecinku
sum_1 += Decimal("0.0111111111111111") # 16 cyfr po przecinku
print("sum: ", sum_1)
sum_1 -= Decimal("0.0222222222222222") # 16 cyfr po przecinku
print("sum: ", sum_1) # 0E-16 ale to dalej jest zero tylko z 16 miejscami po przecinku
print("sum: ", sum_1 == 0) #True

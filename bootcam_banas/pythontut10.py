# rand_list = ["string", 1.234, 28]
# one_to_ten = list(range(11))
# rand_list = rand_list + one_to_ten
# print(rand_list[0])
#
# print("List length: ", len(rand_list))
# first_3 = rand_list[0:3]
# for i in first_3:
#     print("{} : {}".format(first_3.index(i), i))
#
# print(first_3[0] * 3)
# print(first_3* 3)
# print("string" in first_3)
# print("Index of string: ", first_3.index("string"))
# print("How many strings: ", first_3.count("string"))
# first_3[0] = "New string"
# print(first_3)
# for i in first_3:
#     print("{} : {}".format(first_3.index(i), i))
#
# first_3.append("And")
# print(first_3)

#############################
# lista losowych wartosci od 1 do 9
# import random
#
# rand_list = [random.randint(1,9) for i in range(5)]
# print(rand_list)

###########################
# sortowanie bąbelkowe
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at
# the end of the list when the outer loop copmletes 1 cycle
# 3. The inner loop starts comparin indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index +1]
# 5. If so swap the index values
# 6. When the inner loop copletes the largest number is at the end of the list
# 7. Decrement the outer loop by 1
# import random
#
# rand_list = [random.randrange(1,9) for i in range(5)]
# print(rand_list)
#
# i = len(rand_list) - 1
# while i > 1:
#     j = 0
#     while j < i:
#         print("\nIs {} > {}".format(rand_list[j], rand_list[j+1]))
#         print()
#         if rand_list[j] > rand_list[j+1]:
#             print("Switch")
#             temp = rand_list[j]
#             rand_list[j] = rand_list[j+1]
#             rand_list[j+1] = temp
#         else:
#             print("Don't switch")
#         j += 1
#         for k in rand_list:
#             print(str(k) + ",", end="")
#         print()
#     print("End of Round")
#     i -= 1
#     for k in rand_list:
#         print(str(k) + ",", end="")
#     print()

###########################
import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1,9))

num_list.sort()

for k in num_list:
    print(k, end=", ")


num_list.reverse()
print("\n\n")
for k in num_list:
    print(k, end=", ")

num_list.insert(5, 10) # na indeskie 5 wstaw liczbe 10
print(num_list)
num_list.remove(10) # usun element listy korej wartosc to 10
print(num_list)
num_list.pop(2) # usun trzeci od konca elemnt listy
print(num_list)

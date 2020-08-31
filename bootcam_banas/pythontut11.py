# even_list = [i * 2 for i in range(10)]
# for k in even_list:
#     print(k, end=", ")
# print()
#
# import math
#
# num_list = [1, 2, 3, 4, 5]
# list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)] for m in num_list]
#
# for k in list_of_values:
#     print(k)
# print()

# import math
# mult_d_list = [[0]*10 for i in range(10)]
# mult_d_list[0][1] = 10
# # print(mult_d_list[1][1])
# # print(mult_d_list[0][1])
#
# for i in range(10):
#     for j in range(10):
#         mult_d_list[i][j] = "{} : {}".format(i,j)
#
# for i in range(10):
#     for j in range(10):
#         print(mult_d_list[i][j], end=" || ")
#     print()
#
#

#########################
# basic multiplication table
mul_list = [[0] * 9 for i in range(9)] #macierz 10 na 10 same zera
for i in range(len(mul_list)):
    for j in range(len(mul_list[0])):
        mul_list[i][j] = (i+1)*(j+1)

for i in mul_list:
    print(i)
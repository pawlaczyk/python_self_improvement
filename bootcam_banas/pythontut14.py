#import os

# with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
#     my_file.write("Some random text\nMore random text\nAnd some more")

# with open("mydata.txt", encoding="utf-8") as my_file:
#     print(my_file.read())

# print(my_file.closed)

# print(my_file.name)
# print(my_file.mode)
# os.rename("mydata.txt", "my_data.txt")
# os.remove("my_data.txt")

# os.mkdir("mydir")
# os.chdir("mydir")
# print("Current directory: ", os.getcwd())
# os.chdir("..")
# os.rmdir("mydir")

# with open("mydata.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print("Line: ", line_num, ": ", line, end="")
#         line_num += 1


###################################
import os
# with open("mydata.txt", encoding="utf-8") as f:
#     line_num = 1
#     while True:
#         line = f.readline().split()
#         if not line:
#             break
#         print("Num line: ", line_num)
#         print("Words num: ", len(line))
#         print("Avg word: {:.1f}".format(sum(len(i) for i in line)/len(line)))
#         line_num += 1


my_tuple = (1,2,3,4,5,8)
print("1st value: ", my_tuple[0])
print(my_tuple[0:3])
print(len(my_tuple))
more_fibs = my_tuple + (13, 21, 34)
print("34 in tuple: ", 34 in my_tuple)

for i in my_tuple:
    print(i)

a_list = [55, 89, 144]
a_tuple = tuple(a_list)
a_list = list(a_tuple)

print("Max", max(my_tuple))
print("Max", min(my_tuple))
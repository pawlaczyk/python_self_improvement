# try:
#     a_list = [1, 2, 3]
#     print(a_list[3])
# except IndexError:
#     print("Sorry that index doesnt exists")
# except:
#     print("An unknown error occured")
#
#


###########################
# class DogNameError(Exception): #custom exception
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)
#
#
#
# try:
#     dog_name = input("What is you dogs name: ")
#     if any(char.isdigit() for char in dog_name):
#         raise DogNameError #rzucanie cutomowego wyjatku
# except DogNameError:
#     print("Your dog name cant contain number")

###########################
# num1, num2 = input("Enter two values to divide: ").split()
# try:
#     quotient= int(num1) / int(num2)
#     print("{}/{}={}".format(num1, num2, quotient))
# except ZeroDivisionError:
#     print("You cant divide by 0")
# else: #tylko gdy nie wyrzuci wyjatki
#     print("You dind't rase an exception")
# finally:
#     print("I execute no matter what")

###########################
with open("my_data2.txt", "w", encoding="utf-8") as f:
    f.write("One\nTwo\nThree\nfour")

try:
    my_file = open("my_data2.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File: ", my_file.read())
    my_file.close()
finally:
    print("Finally - finished working with file")
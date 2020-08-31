# drink = input("Pick One (Coke or Pepsi): ")
# if drink == "Coke":
#     print("Here is your Coke")
# elif drink == "Pepsi":
#     print("Here is your Pepsi")
# else:
#     print("Here is your Water")


# a, operator, b = input("Enter Calculation: ").split()
# a = int(a)
# b = int(b)
#
# if operator == "*":
#     print(a * b)
# elif operator == "-":
#     print(a-b)
# elif operator == "+":
#     print(a+b)
# elif operator == "/":
#     print(a/b)
# else:
#     print("operator not found")

# age = int(input("Enter Age: "))
# if(age >= 1) and (age <= 18):
#     print("Important birthday")
# elif (age == 21) or (age == 50):
#     print("Important birthday")
# elif not age < 65:
#     print("Importan Birthday")
# else:
#     print("Sory not important")

# age = int(input("enter your age"))
# if age <= 5:
#     print("To young for school")
# if age == 5:
#     print("Got to kindergarden")
# elif (age >= 6) and (age <= 17):
#     print("Go to Grade: ",  age - 5)
# elif age > 17:
#     print("Got to college")
# else:
#     print("Wrong age :<")

# condition
age = int(input("What is your age? "))
can_vote = True if age >= 18 else False
print("You can vote: ", can_vote)
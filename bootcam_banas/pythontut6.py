# print(type("3"))
# print(type('3'))
# print(type("""3"""))
# print(type('''3'''))
#
# sample_string = "This is a very important string"
# print("length: ", len(sample_string))
#
# print(sample_string[0])
# print(sample_string[-1])
# print(sample_string[0:4])
# print(sample_string[8:])
# print("Every other: ", sample_string[0:-1:2])
# print("reverse: ", sample_string[::-1])
#
# print("green" + "eggs")
# print("hello"*5)
# num_string = str(4)
# print(num_string)
#
# for char in sample_string:
#     print(char)
# for i in range(0, len(sample_string)-1, 2):
#     print(sample_string[i] + sample_string[i+1])

# A - Z 65- 90
# a- z 97-122
# print(ord("A"))
# print(chr(65))
#
#
# my_str = input("Enter a string to hide in uppercase")
# secret_string = ""
# for char in my_str:
#     secret_string += str(ord(char))
#
# print("Secret: ", secret_string)
# my_str = ""
# for i in range(0, len(secret_string)-1, 2):
#     char_code = secret_string[i] + secret_string[i+1]
#     my_str += chr(int(char_code))
#
# print("originila: ", my_str)


my_str = input("Enter a string  in uppercase")
secret_string = ""
for char in my_str:
    secret_string += str(ord(char) - 23) # co 122 -23 = 99

print("Secret: ", secret_string)
my_str = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    my_str += chr(int(char_code) + 23)

print("originila: ", my_str)
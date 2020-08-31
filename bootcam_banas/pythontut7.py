# rand_string = "     this is an important string                       "
# rand_string = rand_string.lstrip()
# rand_string = rand_string.rstrip()
# rand_string = rand_string.strip()
#
# print(rand_string)
#
#
# rand_string = "this is an important string"
# print(rand_string.capitalize())
# print(rand_string.upper())
# print(rand_string.lower())
#
#
# a_list = ["Bunch", "of", "random", "words"]
# print(" ".join(a_list))
#
#
# "pig, cow, horse"
# a_list_2 = rand_string.split()
# print(a_list_2)
#
# for i in a_list_2:
#     print(i)
#
# print("ow many is: ", rand_string.count("is"))
# print("ehre is: ", rand_string.find("string"))
# print("replace: ", rand_string.replace(" an ", " a kind of "))
#
# # create acornym
# word = "Random Access Memory"
# acronym = ''.join([i for i in word if 65 <= ord(i) <= 90])
# print(acronym)
#
# word = "random access memory"
# word = word.upper()
# list_of_words = word.split()
# for w in list_of_words:
#     print(w[0], end="")


letter_z = "z"
print("is z a lleter or numner", letter_z.isalnum())
print("is z contains only letter", letter_z.isalpha())
print("is z is digit", letter_z.isdigit())
print("is z is digit", letter_z.islower())
print("is z is digit", letter_z.isupper())
print("is z is digit", letter_z.isspace())


# Caesar cipher
shift = 8
message = "Super tajna wiadomosc z litera xyz".lower()
ciphertext = ""
#encrypt
diff = ord("z") - ord("a") + 1
for i in message:
    letter = ord(i) + shift
    if (ord(i) + shift) < ord("a"):
        letter += diff
    elif (ord(i) + shift) > ord("z"):
        letter -= 26
    ciphertext += chr(letter)
print(ciphertext)


#decrypt
plaintext = ""
for i in ciphertext:
    letter = ord(i) - shift
    if (ord(i) - shift) < ord("a"):
        letter += diff
    elif (ord(i) - shift) > ord("z"):
        letter -= 26
    plaintext += chr(letter)

print(plaintext)

message = input("Enter message: ")
key = int(input("How many charaters shoul we shift? (1-26): "))

secret_message = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char

print("Encrypted: ", secret_message)

# decrypt
key = -key
origin_message = ""
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        origin_message +=  chr(char_code)
    else:
        origin_message += char

print("Decrypted: ", origin_message)
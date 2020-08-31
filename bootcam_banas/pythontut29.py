import re

# ^ : Matches the beginning of string
# $ : Matches the end of the string

# wszystko do małpy
rand_str = "Match everything up to @"
regex = re.compile(r"^.*[^@]")
matches = re.findall(regex, rand_str)
print(len(matches)) # 1
print(matches) # ['Match everything up to ']
print("*"*79)

# wszystko po @ i spacji
rand_str = "@ Get this string"
regex = re.compile(r"[^@\s].*$")
matches = re.findall(regex, rand_str)
print(len(matches)) #1
print(matches) # ['Get this string']
print("*"*79)


# multiline (?m)
rand_str = """Ape is big
Turtle is slow
Cheetah is fast
"""
regex = re.compile(r"(?m)^.*?\s")
matches = re.findall(regex, rand_str)
print(len(matches)) #3
print(matches) # ['Ape ', 'Turtle ', 'Cheetah ']
print("*"*79)

# subexpression - part of the larges expression - nawiasy okrągłe
rand_str = "My number is 412-55-1212" #chcey tylko fragment dostac
regex = re.compile(r"412-(.*)")
matches = re.findall(regex, rand_str)
print(len(matches)) #1
print(matches) # ['55-1212']
print("*"*79)


######################
######################
#dostanie wszystkich numerow calych telefonu
rand_str="412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"\d{3}-\d{3}-\d{4}")
matches = re.findall(regex, rand_str)
print(len(matches)) # 3
print(matches) # ['412-555-1212', '412-555-1213', '412-555-1214']
print("*"*79)

# zeby dostac tylko koncowke numeuru po 412
# (.{8}) dokładnie tylko 8 znaków; tą część którą chcę uzyskać do nawiasu
rand_str="412-555-1212 412-555-1213 412-555-1214"
regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, rand_str)
print(len(matches)) # 3
print(matches) # ['555-1212', '555-1213', '555-1214']
print("*"*79)

##################################
# multiple subexresion -  zwraca tuple
rand_str="My number is 412-555-1212"
regex = re.compile(r"412-(.*)-(.*)")
matches = re.findall(regex, rand_str)
print(len(matches)) # 1
print(matches[0][0]) # 555
print(matches[0][1]) # 1212
print(matches) # [('555', '1212')]
print("*"*79)


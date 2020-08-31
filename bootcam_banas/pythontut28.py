import re

rand_str = "cat cats"
regex = re.compile("[cat]+s?")
matches = re.findall(regex, rand_str)
print(matches)
print("*"*79)

##################
rand_str = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]*")
matches = re.findall(regex, rand_str)
print(matches)
print("*"*79)

#########################
rand_str = "doctor doctors doctor's"
regex = re.compile("[doctor]+['s]{0,2}")
matches = re.findall(regex, rand_str)
print(matches)
print("*"*79)

#####################
# regex na wiersz tekstu
# \n albo \r\n
long_str = '''Just some words
and some more\r
and more
'''
regex = re.compile(r"[\w\s]+[\r]?\n")
print("Matches: ", re.findall(regex, long_str))
for i in re.findall(regex, long_str):
    print(i)
print("*"*79)

###############################
###############################
###############################
# greedy matching - zaschałanne zaznaza wszystko jako jeden wynik
rand_str = "<name>Life On Mars</name><name>Freaks ans Geeks</name>"
regex = re.compile(r"<name>.*</name>")
matches = re.findall(regex, rand_str)
print("Matches: ", len(matches))
print("Matches: ", matches)
for i in re.findall(regex, rand_str):
    print(i)
print("*"*79)

# the smallest match - znak zapytania
rand_str = "<name>Life On Mars</name><name>Freaks ans Geeks</name>"
regex = re.compile(r"<name>.*?</name>") # tylko dopisany znak ?
matches = re.findall(regex, rand_str)
print("Matches: ", len(matches))
print("Matches: ", matches)
for i in re.findall(regex, rand_str):
    print(i)
print("*"*79)


######################
### word boundaries, where words starts ans ends
rand_str = "ape at the apex"
regex = re.compile(r"ape")
regex_2 = re.compile(r"\bape\b") #dopisane \b
matches = re.findall(regex, rand_str)
matches_2 = re.findall(regex_2, rand_str)
print("Matches 1: ", len(matches)) # 2
print("Matches 1: ", matches) #['ape', 'ape']
print("Matches 2: ", len(matches_2)) # 1
print("Matches 2: ", matches_2) # ['ape']

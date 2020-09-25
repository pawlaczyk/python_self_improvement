import re
from functools import reduce

#back references
# \b word boundaries
# wszystkie słowa
rand_str = "The cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+")
matches = re.findall(regex, rand_str)
print(len(matches)) # 6
print(matches) # ['The', 'cat', 'cat', 'fell', 'out', 'the']
print("*"*79)

# znjduje pierwsze słowo z małej litery
# \b word boundaries
# \1 dopisana jedyna \1 - cyfra oznacza subespression, tutja mamy tylko jeden sub
rand_str = "The cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex, rand_str)
print(len(matches)) # 1
print(matches) # ['cat']
print("*"*79)

# back references subsitutions
#pozbycie się tagów <b></b>
rand_str = "<a href='#'><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>") # back reference subsitution
rand_str = re.sub(regex, r"\1", rand_str)
matches = re.findall(regex, rand_str)
print(rand_str) #<a href='#'>The Link</a>
print("*"*79)


# back reference subsittuion
rand_str = "412-555-1212" # chcę wyciągnać osobno 412 i 555-1212
# ([\d]{3}-[\d]{4}) grupuje drugą częśc telefonu - jeden nawias jeden subexpression
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
matches = re.findall(regex, rand_str)
print(len(matches)) #1
print(matches) # [('412', '555-1212')]
# chcemy zmodyfikowac numer telefonu do postaci (412)555-1212
rand_str = re.sub(regex, r"(\1)\2", rand_str)
print(rand_str)
print("*"*79)


#############################
#############################
rand_str = "https://www.youtube.com http://www.google.com"
regex= re.compile(r"(https?://(www\.[\w]+\.[\w]{3}))") #zagneiżdzone suebxpression
# ponizszy nie jest tak dokladny ale wystarczy tutaj
regex= re.compile(r"(https?://([\w.]+))") #zagneiżdzone suebxpression
matches = re.findall(regex, rand_str)
print("Matches: ", matches)
# [('https://www.youtube.com', 'www.youtube.com'), ('http://www.google.com', 'www.google.com')]
rand_str = re.sub(regex, r"<a href='\1'>\2</a>\n", rand_str)
print("New str: ", rand_str)
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='http://www.google.com'>www.google.com</a>
print("*"*79)


#############
# lookahead ?=
# finding information but not returning it
# patrzy na expression ale nie zwraca
rand_str = "One two three four"
regex = re.compile(r"\w+(?=\b)")
matches = re.findall(regex, rand_str) # ['One', 'two', 'three', 'four']
print(matches)
print("*"*79)

# lookbehind (?<=expression)
# finding information but not returning it
# pobieram nazwy porduków po liczbach, ale nie interesują mnie liczby
rand_str = "1. Bread 2. Apples 3. Lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")
matches = re.findall(regex, rand_str) # ['Bread', 'Apples', 'Lettuce']
print(matches)
print("*"*79)

####################
## lookahead and lookbehid
# finding information but not returning it
# wyrazy znajduące się PO otwarciu tagu <h1> LOOKBEGHIND (?<=<h1>)
# wyrazy znajduące się PPRZED zamknięciem tagu </h1> LOOKAEAD (?=</h1>)
rand_str = "<h1>I'm Important</h1> <h1> So am I </h1>"
regex = re.compile(r"(?<=<h1>).*?(?=</h1>)")
matches = re.findall(regex, rand_str) # ["I'm Important", ' So am I ']
print(matches)
print("*"*79)

# negative lookahead and negatie lookbehind
# negative lookaheads (?!expression)
# negative lookbehind (?<!expression)
rand_str = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, rand_str) # ["I'm Important", ' So am I ']
print(matches) # ['8', '1', '1']
matches = [int(i) for i in matches]
print("Total price: {}".format(reduce(lambda x,y: x+y, matches)))
print("*"*79)
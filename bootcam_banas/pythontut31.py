import re
# OR condition
rand_str = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
matches = re.findall(regex, rand_str)
print(len(matches)) # 2
print(matches) # ['Dog', 'Cat']
print("*"*79)

###########
############ zip code with dash
# chcec dostac 12345 12345-1234
rand_str = "12345 12345-1234 1234 12346-322"
regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
matches = re.findall(regex, rand_str)
print(len(matches)) # 2
print(matches) # ['12345 ', '12345-1234']
print("*"*79)

####group
# parts of regular expresion matches
### grupy NUMEROWANE OD 1
# bd = input("Enter your birthday (mm-dd-yyyy) :")
bd = "21-11-2011"
bd_regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)
print("You were born on", bd_regex.group() )
print("BD day", bd_regex.group(1)) # 21
print("BD month", bd_regex.group(2)) # 11
print("BD year", bd_regex.group(3)) # 2011
print("*"*79)


# match objects functions
match = re.search(r"\d{2}", "The chickend weight 13 lbs")
print("Match: ",match.group()) # 13
print("Span: ", match.span()) # (20,22)
print("Start: ", match.start()) # 20
print("End: ", match.end()) # 22
print("*"*79)


# named groups
#nazwana grupa (?P<nazwagrupy>regex)
rand_str = "December 21 1974"
regex = re.compile(r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)")
matches = re.search(regex, rand_str)
print(matches) # <re.Match object; span=(0, 16), match='December 21 1974'>
print("Moth: ", matches.group("month")) #December
print("Day: ", matches.group("day")) # 21
print("Year: ", matches.group("year")) # 1974
print("*"*79)


#########################
########################
# wyciagnac wszystkie adresy email
rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
regex = re.compile(r"[a-zA-Z][\w\-+_]+@[\w\-+_]+\.[\w\-+_\.]+")
regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = re.findall(regex, rand_str)
print(matches) # ['d+b@aol.com', 'a_1@yahoo.co.uk', 'A-100@m-b.INTERNATIONAL']
print("*"*79)

#########################
########################
# znaleźc wszystkie numery telefonu
rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-55-1212"
regex = re.compile(r"\d{11}|\d{10}|\(\d{3}\)\d{7}|\d{3}\s\d{4}|\d{3}-\d{3}-\d{4}|\d-\d{3}-\d{2}-\d{4}")
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4}|\d{4}))")
# (1?) jedynak w nawiasie moze byc moze nie byc
# (-| ?) myslnik moze byc moze nie byc LUB spacja moze byc moze nie byc
# (1?)(-| ?)(\())? ta czesc moze byc moze nie byc
# (\d{3}) trzy liczby zawsze są
# (\)|-| |\) może byc nawias zamykacjay, myslnik albo spacja
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)
print("*"*79)
import re

rand_str = "F.B.I. I.R.S. CIA"
print("Mathes: ", len(re.findall(".\..\..", rand_str)))

rand_str = """This is long
string that goes
on for many lines"""
print(rand_str)
print("*"*79)

# kompilowanie regexu
regex = re.compile("\n")
rand_str = regex.sub(" ", rand_str)
print(rand_str)
print("*"*79)

# \b \f \r \r \v - vertical tabs \r\n - Windows
rand_str = "12345"
#\d to samo co [0-9]
# \D [^0-9] wszysctko po za cyframi
print("Matches: ", len(re.findall("\d", rand_str)))
print("*"*79)


# 5 cyfrowe liczby
rand_str = "12345"
if re.search("\d{5}", rand_str):
    print("it is a zip code")

print("*"*79)

# 5, 6, 7 cyfrowe liczby
rand_str = "123 12345 123456 1234567"
print("Matches: ", len(re.findall("\d{5,7}", rand_str)))
print("*"*79)


# sprawdzanie numeru telefonu
# \w [a-zA-Z0-9]
# \W [^a-zA-Z0-9]
ph_num = "412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}",ph_num):
    print("It is a phone number")
print("*"*79)

#sprawdzanie dlugosci slowa
name = "Ultraman"
if re.search("\w{2,20}",name):
    print("It is a valid name")
print("*"*79)

# whitechar
# \s [\f\n\r\t\v]
if re.search("\w{2,20}\d\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid name")

# ciągi liter "a", "aa", "aaa", "aaa...a"
print("Matches :", len(re.findall("a+", "a as ape bug"))) #3


# 1. 1 to 20 lowercase and uppercase leters, number, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase ans uppercase letters, number, plux .-
# 4. a period
# 5. 2 to 3 lowercase and uppercase letters
email_list = "db@aol.com m@.com @apple.com db@.com"
regex = re.compile("[\w.%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}")
print("Email Matches :", len(re.findall(regex, email_list)))
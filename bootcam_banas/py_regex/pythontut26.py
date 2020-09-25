import re

#re.search
if re.search("ape", "The ape as the apex"):
    print("There is an ape")
print("*"*79)

# re.findall lista wszystkich znalezionych
all_apes_list = re.findall("ape", "The ape was at the apex")
for i in all_apes_list:
    print(i)
print("*"*79)

# iterator re.finditer
# iterator_obiek.span() zwraca pozycje tuple (pozycja_nr_poczatek, pozycja_nr_koniec)
the_str = "The ape was at the apex"
for i in re.finditer("ape.", the_str): # "ape." kropka - jeden znak albo spacja
    loc_tuple = i.span()
    print(loc_tuple) #Zwraca (4, 8) i (19, 23) pozycje
    print(the_str[loc_tuple[0]:loc_tuple[1]])

# (4, 8)
# ape
# (19, 23)
# apex
print("*"*79)


# match for specific letters
#re.findall
# [crmfp]at - cat, rat, mat, fat, pat
animal_str = "Cat rat mat fat pat" # [crmfp] pierwsza litera wyrazu musi byc z zakresu
some_animals = re.findall("[crmfp]at", animal_str) #"Cat" jest z wielkiej litery i nie trafi tutaj
for i in some_animals:
    print(i)
# rat
# mat
# fat
# pat
print("*"*79)

# match for specific letters
#re.findall
# [c-mC-M]at - cat, dat, eat, fat ... mat, Cat, Dat, Eat, Fat ... Mat
animal_str = "Cat rat mat fat pat"
some_animals = re.findall("[c-mC-M]at", animal_str) # [c-mC-M] zakresy pierwszej listery
for i in some_animals:
    print(i)
# Cat
# mat
# fat
print("*"*79)


# exclude ^  wykluczenie
# [^Cr]at wszystkie po za Cat, rat;  ALE spacja tez może być jako pierwszyszy znak
animal_str = "Cat rat mat fat pat at" # "Cat" zacyzna się od wielkiej litery "C", tak samo nie złapie "rat" przez "r"
some_animals = re.findall("[^Cr]at", animal_str) # ^ poza literami C, r
for i in some_animals:
    print(i)
# mat
# fat
# pat
#  at
print("*"*79)

# zamiana
# re.sub - zamiana
# re.compile - tworzenie obiektu wzorca
owl_food = "rat cat mat pat"
regex = re.compile("[cr]at")
owl_food = regex.sub("owl", owl_food)
print(owl_food)
# owl owl mat pat
print("*"*79)

# backlshashe
# re.search
# raw string jako argument - (r"szukanyString", zmienna)
rand_str = "Here is \\stuff"
print("Find \\stuff :", re.search("\\stuff", rand_str))
# Find \stuff : None
print("Find \\stuff :", re.search("\\\\stuff", rand_str))
# Find \stuff : <re.Match object; span=(8, 14), match='\\stuff'>
# surowy string
print("Find \\stuff :", re.search(r"\\stuff", rand_str))
# Find \stuff : <re.Match object; span=(8, 14), match='\\stuff'>
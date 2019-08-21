#Real world example
"""
Udemy kurs Python intermidiate
"""
#powiedzmy że mamy ogromny plik z logami i chcemy posumowac ile tych bajtów przyszło (ostania kolumna w wierszu)
################## z funkcjami #####################
wwwlog = open('duzy_plik_z_logami.log')
for line in wwwlog:
    print(line)
    break

wwwlog = open('duzy_plik_z_logami.log')
total = 0

for line in wwwlog:
    bytestr = line.rsplit(None, 1)[1]
    if bytestr != '-':
        total += int(bytestr)

print("Total: ", total)


################## z generatorami #####################
# piękny śliczny cudowny słodziutki kod dzięki generatorom <3
wwwlog = open('duzy_plik_z_logami.log')
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')

print("Total: ", sum(bytes))

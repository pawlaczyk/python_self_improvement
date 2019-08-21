#coding = utf-8
"""
"EFEKTYWNY PYTHON - 59 sposobów na lepszy kod" 
Rozdział 1
"""

# --------------------------------------------------------------------

# 1 Kodowanie znaków: bytes vs str vs unicode
# 1.1 Zmiana unicode -> bin
# funkcja encode()
a = u'Alą'
# >>> a
# 'Alą'
a.encode()
# b'Al\xc4\x85'
type(a)
# <class 'str'>
type(a.encode())
# <class 'bytes'>

# 1.2 bin->str
b = 'wąż'.encode()
# b'w\xc4\x85\xc5\xbc'
b.decode()
# 'wąż'

# --------------------------------------------------------------------

# 2 Funkcje pomocnicze
# 2.1 bajty -> stringi
def to_str(bytes_or_str):
    """
    Funkcja zamieniajaca bajty na stringi
    bin -> str
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8') #zamienia na stringi
    else:
        value = bytes_or_str
    return value #

# 2.2  string -> bajty
def to_bytes(bytes_or_str):
    """
    Funkcja zamieniajaca stringi na bajty
    str -> bin
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode() #zamienia na bajty
    else:
        value = bytes_or_str
    return value

# --------------------------------------------------------------------

# 3. Otwieranie pliku 
# 3.1 Otwieranie binarnego pliku
def open_binary_file(filepath):
    """
    Otwiera plik binarnie do zapisu
    """
    with open(filepath, 'wb') as f:
        f.write(os.urandom(10)) 

def open_str_file(filepath):
    """
    Otwiera plik w znakach zakodowanych w utf-8 do zapisu
    """
    with open(filepath, 'w') as f:
        f.write(os.urandom(10)) 

# --------------------------------------------------------------------

# 4 Zamiast skomplikowanych wyrażen stosuj funkcje pomocnicze
# 4.1 Pobieranie wartosci w nieczytelny sposob
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                    keep_blank_values=True)
print(my_values)
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

print("-------------------------------------------")

# 4.2 Pobieranie wartosci ze slownika za pomoca metody get 
# get pobiera wartosc zależnie od nazwy klucza
print('Czerwony: ', my_values.get('red'))
print('Zielony: ', my_values.get('green'))
print('Krycie: ', my_values.get('opacity'))
print('Pusty: ', my_values.get('pusty')) #Zwraca None

print("-------------------------------------------")

# 4.3 Wypisywanie z wyrazeniem bollowski or 
# do ladnego zwracania danych, a nie że raz pusty string w  lista czy None
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Czerwony: %r' % red)
print('Zielony: %r' % green)
print('Krycie: %r' % opacity)
# Czerwony: '5'
# Zielony: 0
# Krycie: 0

# 4.4 Nieczytelny jednolinijkowiec
red = int(my_values.get('red', [''])[0] or 0) #Nieczytelny jednolinijkoweic

# 4.5 Czytelniejsze wyrazenie if-else
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

# 4.5 CZYTELNIE - pelna konstrukcja if-else
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

# 4.5 Zamiana CZYTELNEJ formy na funkcje pomocnicza
# Należy tak robić, jeżeli mamy zamiar wielokrotnie używać 
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')

print("-------------------------------------------")
print(red)
print(green)
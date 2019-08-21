#coding=utf-8

"""
Dekorator gdzie do obiektu pliku dodajemy jakieś logowanie
rozwiązanie problemu gdzie wzorzec dekorator - jego APio nie pozwalało na wykorzystanie metod będących na obiekcie
bazowycm, który dekorator dekorował (dodawała jakeiś extra funckjonalności

1. Pierwszym naiwnym rozwiazaniem mógłbyby być kopiowanie całego interfejsu elementu będącego atrybutem dekoratora
ale to nie jest w praktyce zbyt dobre roziazanie = > tutaj szukamy czegoś bardizej automatycznego
(typowo trzeba redefiniowac wszsytkie metody który ma obiekt)
"""

class FileWithLogging:
    """WAŻNE: traktujemy plik z logowaniem jakby był plikiem!
    Te opakowujące file metody sa wystarczające być miec dostęp do wszsytkich metoda jakie posiada file - nie trzeba
    reimplemetnować CAŁEGO API/ Interfejsu klasy File
    Jest to mozliwe dizęki rozbienie proxy i wszsytkich magicznym procesom jakie są niżej zdefiniowane

    Minusem jest spadek wydajnośći poniewż poniewaz uruchamiane są metody na dekorowanym obiekcie a każde wywołanie
     niesie ze soba jakiś koszt ale na szczęscie jest to tylko bardzo mały koszt

    Elastycznosć na którą możemy sobie pozwolisc z tym wzorcem pozwala na Łatwe obudowywawanie nawet wielkieog API
    przy użyciu takiego dekoratora. gdyby zastosowac klasyczne proxy to trzeba zreimplemnetowac każdą , naprawdę
    każda metodę wystepująca na obieckie file - a to jest brdzo nieprawktyczne
    Całośc - takie pobiewranie metod z __getattr__ jest mozliwe tylko dizęki dynamicznemu programowaniu
     """
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        #traktujemy fielWithLogging jak file -  udostepniania metody z file
        return self.file.__iter__()

    def __next__(self):
        #traktujemy fielWithLogging jak file -  udostepniania metody z file
        return self.file.__next__()

    def writelines(self, strings):
        self.file.writelines(strings) #przkierowanie do obiektu na który mamy referencję
        print(f'wrote {len(strings)} lines')

    def __getattr__(self, item):
        """traktujemy fileWithLogging jak plik"""
        return getattr(self.__dict__['file'], item) #dobieranie się do metod jai ma podstawowy obiekt

    def __setattr__(self, key, value):
        #takie proxy gdzie wykonujemy operacje na wewnetrznym niewidocznym bazwoych obiekcie do którego mamy referencję
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key) #ustawienie atrybuty na obiekcie bazwoych

    def __delattr__(self, item):
        #plik też ma taką metodę - takie proxy gdzie wykonujemy operacje na wewnetrznym niewidocznym bazwoych obiekcie do którego mamy referencję
        delattr(self.__dict__['file'], item)

if __name__ == "__main__":
    #teraz moze zwykły plik opakowac w tę ^ implementację
    file = FileWithLogging(open('hello.txt', 'w'))
    #poniewąz zaimplemetowaliśmy metody z pliku w taki sposób że wykorzystywany jest bazowy obiekt pliku - tak naprawde przekierowujemy wywołania do bazowego pliku
    file.writelines(["hello", "world"]) #wrote 2 lines
    file.write("Wywołanie metody bezpośrednio na pliku bo mamy zdefiniowane __getattr__") #helloworldWywo�anie metody bezpo�rednio na pliku bo mamy zdefiniowane __getattr__
    file.close() #dizęki __getattr__ mamy możliwość bezpośredniego wywołania etody na obiekcie

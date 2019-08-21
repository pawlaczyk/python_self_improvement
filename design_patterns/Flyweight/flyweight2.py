#coding=utf-8
"""
Przykład z formatowaniem tesktu - dodawanie styli jak w edytorze tekstowym
"""


class FormatText:
    """
    1. Wersja brute force - tworzymy listę bool długą jak tekst i zapisuje informację o każdej lieterze czy ma być
     z wielkiem czy z małej
    """
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text) #niepotrzebnie przechowujemy aż tyle

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return ''.join(result)


class BetterFormatedTest:
    """ `self.formatting` bedzie przechoywanc OBIEKT flyweigh mający tylko start, end liter (i dodatkowo styl capitalize)
     które mają być z wielkiej - jesli mamy milion slów a tylko jeden wyraz jest z wielkiej to na cholere nam tyle booli co ma sam teks"""
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = [] #przechowuje liste obiektów TextRange będącego implementacją wzorca flyweight

    #klasa wewnętrzna - rozwiązanie z  wzorca flyweight
    class TextRange:
        """zamiast capitalize można dać jakikolwiek inny styl
        Esenscja wzroca flyweight - możesz zwrócić flyweight aale także możesz przechowywac flyweigh """
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        """metoda która pokrywa """
        def covers(self, position):
            return self.start <= position <= self.end #po prostu warunki logidzne z zakresu

    def get_range(self, start, end):
        """Dzięki temu można modyfikowac poźniej tekst jak sie zmieniło zdania z małcyh na duże
        i w drugą stronę wieloktrotnie"""
        range = self.TextRange(start, end)
        self.formatting.append(range) #glówna klasa przechowuje teraz zakres wielkich liter
        return range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)

        return ''.join(result)




if __name__ == "__main__":
    #wersja 1
    text = "This is a brave new world"
    ft = FormatText(text)
    ft.capitalize(10, 15)
    print(ft)  # This is a BRAVE new world


    #wersja 2
    bft = BetterFormatedTest(text)
    bft.get_range(16,19).capitalize = True
    print(bft)

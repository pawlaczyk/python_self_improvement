#coding=utf-8


class WindowInterface:
    def build(self): pass


class AbstractWindowDecorator(WindowInterface):
    """Maintain a reference to a Windows object and define an interface that conforms to Windows's interface
    abstrakcyjny dekorator jest niewidoczny dla klienta który dodaje funkcjonalności do okna przez opakowanie go
     dekoratorami """

    def __init__(self, window):
        self._window = window #klasy dziedziczące eż mają ten atrybut oniektu Windows

    def build(self): pass #Abstrakcyjny dekorator - abstrakcyjna metoda `buils` konkretny dekorator dodaje
    # rodzaj funkcjonalnosci według swojej impolmentacji


class Window(WindowInterface):
    def build(self):
        print("Building Window") #obiekt który jest dekorowany - on sam w sobie nie jest modyfikowany, dekorator
        # rzeczywiście tworzy nowe rzeczy i dodaje funkcjonalności ale potem tylko wywołuje metodę obiektu tej klasy na nim


class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print("Adding border") #dodatkowa funckjonalność dekoratora

    def build(self):
        self.add_border() #dodanie funkcjonalności przez dekorator
        self._window.build() #metoda wywoałan na obiekcie

class VerticalSBDecorator(AbstractWindowDecorator):
    def add_vertical_scroll_bar(self):
        print("Adding vertical scroll bar") #dodatkowe funckjonalności które moze nadac dekorator

    def build(self):
        self.add_vertical_scroll_bar()#dodanie dynamiczne funcjonalnosći przez dekoator
        self._window.build() #metoda wywołana na obiekcie

class HorizontalSBDecorator(AbstractWindowDecorator):
    def add_horizontal_scroll_bar(self):
        print("Adding horizontal scroll bar") #dodatkowe funckjonalności które moze nadac dekorator

    def build(self):
        self.add_horizontal_scroll_bar()#dodanie dynamiczne funcjonalnosći przez dekoator
        self._window.build() #metoda wywołana na obiekcie


if __name__ == "__main__":
    #przykład budowania różnych rodzai okien

    #1. udowanie okna - obiketu któremu dynamicznie dodajemy funkcjonalności przez opakowanie go dekoratorami
    window = Window()
    window.build()

    windows_with_border = BorderDecorator(window)
    windows_with_border.build()
    window_with_border_with_vertical = VerticalSBDecorator(windows_with_border) #kombinaja dwóch dekoratorów - dynamiczne dodanie dwóch funcjonalności obiektowi window
    window_with_border_with_vertical.build()

    window_with_border_with_vertical_with_horizontal = HorizontalSBDecorator(window_with_border_with_vertical)
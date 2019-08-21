#coding=utf-8

#adapter wersja z buforowaniem - cache

class Point:
    def __init__(self, x, y):
        self.y =y
        self.x = x

def draw_point(p):
    """takie API dostaję i musze je używać - być z nim kompatybilna
    Punk jest rysowany jako kropka bez żadnych łman linii"""
    print('.', end='')



class Line:
    """To chce użyć
    W naszym przypadku musmy reprezentować linię jako serie punktów w kolejnośći by być zdolnym do narysowania czegokolwiek
    inaczej to po prostu nie zadziała => musimy zbudować adapter jakieś z lini do punktów adapter"""
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    """Prostokąt składa się z czterech linii ale rysowanie jest możliwe tylko i wyłącznie przez `draw_point`
    przyjmującego punkty """
    def __init__(self, x,y, width, height ):
        super().__init__()
        self.append(Line(Point(x,y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x,y), Point(x, y+height)))
        self.append(Line(Point(x,y+height), Point(x + width, y +height)))


class LineToPointAdapter():
    """Ilustracja jak prosty cache może zredukowac liczbę generowanych obiektów tymczasowych podczas implementacji wzorca Adapter
     """
    #rozwiazanie nadmiernego generowania tymczasowych obiektów - cache jest słownikiem
    cache = {}

    def __init__(self, line):
        self.h = hash(line) #obliczy unikalną wartość dla każdej pojedynczej linii jak klucz naszego słownika
        if self.h in self.cache:
            return # jeśli wartośc jest już w słowniku cache to już nie wyśiwetlamy punktów i nie generujemy tymczasowych punktów


        print(f'Generating points for line ' #wynokue się tylko raz dla takiej samej listy punktów
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]')


        points = []

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x,top)) # adapter już nie dziedziczy po liście - żeby iterowac po nim trzeba implementować metodę __iter__

        self.cache[self.h] = points #niestatyczny atrybut który można użyć później by otrzymać dostęp do poszczególnej wartości cache
        # teraz adapter nie jest sam listaą i teraz tak naprawde iterujemy po wartości cache

    def __iter__(self):
        # umożliwia iterowanie po adaperze który nie musi teraz dziedzczyć po liście
        #umożlwiia iterowanie po całym zbiorze dostępnych danych i po tym iterujemy
        return iter(self.cache[self.h])


def draw(rcs):
    print('\n\n----- Drawing some stuff -----\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter: #adapter implementuje metodę __iter__ - możemy fo tutaj używać jak listy
                draw_point(p)



if __name__ == "__main__":
    #1. wyobrażamy sobie sytuację gdy mamy wiele prostokątów
    # problem jest taki że chcemy je narywoać - musimy mieć jakąś funkcję rysującą je
    rcs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,6,6)
    ]

    draw(rcs) #wyświetla się tylko za pierwszym razem
    draw(rcs)
    draw(rcs)
    draw(rcs)

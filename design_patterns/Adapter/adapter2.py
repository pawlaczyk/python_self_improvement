#coding=utf-8

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


class LineToPointAdapter(list):
    """Problem adaptera jest takiż, e generuje tymczasowe obiekty ponieważ gdy adaptujemy lnię do punktu to
     musimy wygenerować wiele punktów (np. podczas wielokrotnego uzywanie adapteraz z tą samoą listą prostokątów)

    Pytanie jest czy musimy za każdym razem wciaż i wciąż generować tyle obiektów tymczasowych?
     """
    count = 0 # przechowujemy liczbę punktów bo będzie ich generowac bardzo dużo

    def __init__(self, line):
        super().__init__()
        self.count += 1 #przechowujemy właściwie liczbę jak wiele wywołać zrobiliśmy

        print(f'{self.count}: Generating points for line '
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]')


        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x,top)) #jest lista wiec możemy w draw(rcs) w petli for p in adapter używać adaptera




def draw(rcs):
    print('\n\n----- Drawing some stuff -----\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter: #adapter jest listą - możemy fo tutaj używać
                draw_point(p)



if __name__ == "__main__":
    #1. wyobrażamy sobie sytuację gdy mamy wiele prostokątów
    # problem jest taki że chcemy je narywoać - musimy mieć jakąś funkcję rysującą je
    rcs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,6,6)
    ]

    draw(rcs)
    draw(rcs) #generowanie po raz kolejnych w adapterze tymczsowych obiektów punktów
    draw(rcs) #generowanie po raz kolejnych w adapterze tymczsowych obiektów punktów
    draw(rcs) #generowanie po raz kolejnych w adapterze tymczsowych obiektów punktów

#coding=utf-8

class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass


# Target interface
class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    #brak metody earth


#Adaptee
class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

#Client
class AmericanKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110: #Amerykański czajnik wymagam mniejszej ilosci woltów
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


class Adapter(USASocketInterface): #implementuje interfejs Amerykański
    """adapter z amerykańskiego czajnik do Europejskiego gniazda
    adapter jednostronny - typowy
    """
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110 #nadpisuje wolty tak by wartosc pasowala do Amerykańskiego czajnika

    def live(self):
        return self.__socket.live() #ni3 nadpisuje po prostu zwraca wartosći z gniazda

    def neutral(self):
        return self.__socket.neutral()


if __name__ == "__main__":
    #tak naprawde nie widoczny jest USASocketInterface przy używaniu czajnika przez klienta
    european_socket = EuropeanSocket()
    american_kettle = AmericanKettle(european_socket) #uruchomieie amerykańskiego czajnika z europejskim gniazdem
    american_kettle.boil() #Kettle on fire! bo     EuropeanSocket.voltage()  zwraca 230 co jest za dużo dla emarykańskiego czajnika

    adapter = Adapter(european_socket) #adapter opakowuje europejskie gniazdo gdzie adpater bierzez dane z europejskie wtyczki i nadpisuje/modyfikuje dostane wartosci tak by zwrócić ynik dobry dla czajnika
    american_kettle = AmericanKettle(adapter) # do czajnika podłączamy opakowane już europejskie gniazdo, czajnika interesują tylko metody z obiektu socket które wywołuje
    american_kettle.boil() #Coffee time! bo adapter zwrócił w self.__power.voltage() wartość 110 opowiadającaklientowi

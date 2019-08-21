#coding=utf-8
import re
dataRaportu = ""
godzinaRaportu = ""
hostUp= ""

class DivisionBlock():
    def __init__(self, ip , name='name', portList, system = "Nie Zanleziono"):
        self.hostAddress = ip
        self.name = name
        self.portsList = None
        self.portFunction = None
        self.text = None
        self.device = device
        self.system = system
    def addText(self, text):
        self.text = text
    def __str__(self):
        return str(self.hostAddress) +" "+ str(self.name) + str(self.system)


listOfBlock = []


def cutTopDown(plikNazwa):
    """1) Funkcja wstępnie przetwarzająca tekst  """

    licznikBlokow = 0
    toCut = ('SF:', 'Uptime guess', 'TCP Sequence', 'SYN', 'Increasing', 'Warning:',
             'Completed', 'Discovered','</output>', '<?xml', 'Initiating NSE', 'NSE:',
             'Retrying OS detection', 'Scanning', 'Initiating', 'Service scan Timing',
             'Starting Nmap', 'Network Distance:', 'No exact OS matches', 'IP ID Sequence',
             'Service Info:')
    wynikowy = open("wynikowy.xml", 'w')
    with open('skanNmap.xml') as fileXml:
        lines = fileXml.readlines()
        for l in lines:
            flaga = True
            line = l.split('\n')
            line = str(line).replace("[", "")
            line = str(line).replace("]", "")
            line = str(line).replace("'", "")
            line = str(line).replace("'. ''","" )

            if str(line).startswith('Starting Nmap' ):
                flaga = True
                global dataRaportu
                global godzinaRaportu
                dataRaportu = str(line).split()[-3]
                godzinaRaportu = str(line).split()[-2]
            if 'Nmap scan report for' in str(line):
                flaga = True
                ip =  line[0].split(' ')[-1]
                newIP = ip.replace("(", "")
                ip = newIP.replace(")", "")
            if str(line).startswith('HOP RTT'):
                flaga = False
            if 'ms' in str(line):
                flaga =False
            if str(line).startswith('-  '):
                flaga = False
            if '... ' in str(line):
                flaga = False
            if str(line).startswith(toCut):
                flaga = False
            if 'TRACEROUTE' in str(line):
                flaga = False
            if flaga == True:
                if line.split()[-1] == ',':
                    licznikBlokow += 1
                    if licznikBlokow % 2 == 0:
                        wynikowy.write('\n')
                    else:
                        pass
                else:
                    wynikowy.write(str(line) + "\n")

    return "wynikowy.xml"

def findIPName(line):
    """ Funkcja znajdująca adresy ip oraz nazwy jesli są"""
    ip = line[0].split(' ')[-2]
    newIP = ip.replace("(", "")
    ip = newIP.replace(")", "")
    name = line[0].split(' ')[-3]
    if str(name) == "for":
        name = "NULL"
    return ip, name

def findPortNumber(line):
    """Funkcja wyszukujaca numery portów i rodzaje usługi Tcp lub Udp"""
    if '/tcp' in str(line).split()[0]:
        portAddress = str(line).split()[0].replace("['", "").split('/')[0]
        TcpOrUdp = str(line).split()[0].replace("['", "").split('/')[1]
        openFiltered = str(line).split()[1]
        usluga = str(line).split()[2].split('/')[0]
        return portAddress, TcpOrUdp, openFiltered, usluga
    else:
        return False

def findDevice(line):
    device = str(line).replace('[', '')
    device = str(device).replace(']', '')
    device = device.replace('general purpose', '')
    device = device.replace("', ''", "")
    device = device.replace("|", " ")
    device = device.replace(",", "")
    device = device.replace("'", "")
    device = device.split(':')[1]
    device = device.split()

    return device


def filtrFile(wynikowy_A):
    """2) Funkcja filtrująca częściowo przetworzony tekst"""
    with open(wynikowy_A) as fileXml:
        for line in fileXml:
            line = line.split('\n') #listy bardziej elastyczne niż krotki
            ip = ""
            name = ""
            TcpOrUdp =""
            openFiltered = ""
            usluga = ""
            system = []
            if 'Nmap scan report for' in str(line): #pierwsz
                ip,name = findIPName(line)
            if findPortNumber(line) != False :#porty
                ip, TcpOrUdp, openFiltered, usluga = findPortNumber(line)
                #print ip, TcpOrUdp, openFiltered, usluga
            if 'Device' in str(line):
                device = findDevice(line)
            if 'Aggressive OS guesses:' in str(line): #systemy
                system = str(line).split(':')[1]
            if 'Nmap done:' in str(line): #hostUP
                global hostUp
                hostUp = str(line).split('(')[1].split()[0]
            if  str(line) == '\n':



def main():
    wynikowyA = cutTopDown('nmapSkan.xml')
    filtrFile(wynikowyA)

if __name__ == "__main__":
    main()
#coding=utf-8
#z daty id skan zrobić data + random idskanu
import re
dataRaportu = ""
godzinaRaportu = ""
hostUp= ""
listOfBlock = []
liczbaHostowWSieci = ""

class Block():
    def __init__(self, ip, name,latency,  portList, device, system, portInformacje):
        self.ip = ip
        self.name = name
        self.latency = latency
        self.portsList = portList
        self.device = device
        self.system = system
        self.portInformacje = portInformacje

def cutTopDown(plikNazwa):
    """1) Funkcja wstępnie przetwarzająca tekst  """

    licznikBlokow = 0
    toCut = ('SF:', 'Uptime guess', 'TCP Sequence', 'SYN', 'Increasing', 'Warning:',
             'Completed', 'Discovered','</output>', '<?xml', 'Initiating NSE', 'NSE:',
             'Retrying OS detection', 'Scanning', 'Initiating', 'Service scan Timing',
             'Starting Nmap', 'Network Distance:', 'No exact OS matches', 'IP ID Sequence',
             'Service Info:', 'SF-Port')
    wynikowy = open("wynikowy.xml", 'w')
    with open(plikNazwa) as fileXml:
        lines = fileXml.readlines()
        for l in lines:
            flaga = True
            line = l.split('\n')
            line = str(line).replace("[", "")
            line = str(line).replace("]", "")
            line = str(line).replace("'", "")
            line = str(line).replace("'. ''","" )

            if '|_' in str(line):
                line.replace('|_', '|_ ')

            if  'CEST' in str(line):
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
                if '| ,' in str(line):
                    line = line.replace('| ,', '')
                if line.startswith(','):
                    licznikBlokow += 1
                    if licznikBlokow % 2 == 0:
                        wynikowy.write('###\n')
                    else:
                        pass
                else:
                    wynikowy.write(line + '\n')

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
    try:
        device = device.split(':')[1]
    except IndexError:
        pass
    device = device.split()
    return device

###############################################3
#Paskudne zakresy na globalnych zmiennych ale dziala - brak nonlocal z 3.0
device = []
latency = 'NULL'
ip = ""
name = ""
TcpOrUdp = ""
openFiltered = ""
portList = []
usluga = ""
dodatkoweInformacje = []
portAddress = ""
system = []
portFunction = {}
portInformacje = {}
##################################################33

def changeGlobalTextVariable():
    global ip
    global latency
    global name
    global TcpOrUdp
    global openFiltered
    global portList
    global usluga
    global portAddress
    global device
    global system
    global portFuncion
    global dodatkoweInformacje
    global portInformacje

    ip = ""
    latency = 'NULL'
    name = ""
    TcpOrUdp = ""
    openFiltered = ""
    portList = []
    usluga = ""
    portAddress = ""
    system = []
    portFunction = []
    dodatkoweInformacje = []
    portInformacje = {}

def filtrFile(wynikowy_A):
    """2) Funkcja filtrująca częściowo przetworzony tekst"""

    with open(wynikowy_A) as fileXml:
        for line in fileXml:
            line = line.split('\n') #listy bardziej elastyczne niż krotki

            if 'Nmap scan report for' in str(line): #
                global ip
                global name
                ip,name = findIPName(line)

            if 'Host is up' in str(line):
                global latency
                latency = str(line).split('(')[1].split(' ')[0]

            if findPortNumber(line) != False :#porty
                global portAddress
                global TcpOrUdp
                global openFiltered
                global usluga
                global portList
                global dodatkoweInformacje
                global portInformacje

                portInformacje[portAddress] = dodatkoweInformacje

                #print portInformacje
                #print ip, portAddress, dodatkoweInformacje
                dodatkoweInformacje = [] #czyszczenie dla kazdego portu

                portAddress, TcpOrUdp, openFiltered, usluga = findPortNumber(line)
                portList.append((portAddress, TcpOrUdp, openFiltered, usluga))

            if 'Device' in str(line):
                global device
                device = findDevice(line)

            if 'Aggressive OS guesses:' in str(line): #systemy
                global system
                system = str(line).split(':')[1]
                #print system

            #dodatkowe informacje np szyfry etc
            if  "['|_" in str(line).split(' ')[0] or str(line).split(' ')[0] == "['|" or str(line).split(' ')[0] == "['|_": #
                line = str(line).replace("['|_", '')
                line = str(line).replace("['|", '')
                line = str(line).replace("']", '')
                line = str(line).replace(", '", '')
                dodatkoweInformacje.append(line)

            if 'Nmap done:' in str(line): #hostUP
                global hostUp
                global liczbaHostowWSieci
                hostUp = str(line).split('(')[1].split()[0]
                liczbaHostowWSieci = str(line).split(':')[1].split(' ')[1]
            if  '###' in str(line):
                global listOfBlock
                #print portInformacje
                #print latency
                #print ip, name, portList, device, system
                b = Block(ip, name,latency, portList, device, system, portInformacje)
                listOfBlock.append(b)
                changeGlobalTextVariable()

def printObjects(listOfBlock):
    for i in listOfBlock:
        print i

def returnObjects():
    global listOfBlock
    return listOfBlock
def returnDate():
    return dataRaportu


def main():
    #wynikowyA = cutTopDown('xml0.xml')
    #wynikowyA = cutTopDown('xml1.xml')
    #wynikowyA = cutTopDown('xml2.xml')
    #wynikowyA = cutTopDown('xml3.xml')
    #wynikowyA = cutTopDown('xml4.xml')
    #filtrFile(wynikowyA)
    #printObjects(listOfBlock)

    return listOfBlock, dataRaportu, godzinaRaportu, hostUp, liczbaHostowWSieci



if __name__ == "__main__":
    main()
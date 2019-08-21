#coding=utf-8
import MySQLdb
import logging
import main2
"""
Pola obiektu
        self.ip = ip #str 193.9.121.16
        self.name = name #str NULL / opos.billbird.pl
        self.latency = latency #str 0.0066s
        self.portsList = portList #lista ('179', 'tcp', 'open', 'tcpwrapped,')
        self.device = device #list ['storage-misc', 'firewall', 'switch', 'WAP', 'load', 'balancer']
        self.system = system Linksys BEFW11S4 WAP (87%), Linux 2.6.32 (87%), ', ''] #str
        self.portInformacje = portInformacje  ('443', 'tcp', 'open', 'ssl') #dict

"""
""" Klucze obce : alter table klienci add foreign key(`kraj`) references kraje(`id`); """

#--------------------------------------------------------- Połączenie z bazą -------------------------------------------
def connectToDatabase(name):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="admin",  # your password
                         db=name)        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    print "Połączono"
    # tworzenie tabel
    # execute SQL query using execute() method.
    cur.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cur.fetchone()

    print "Database version : %s " % data

    sql = " USE " + name + " ;"
    cur.execute(sql)
    return cur, db
#--------------------------------------------------------- Tworzenie Tabel -------------------------------------------
#Administratorzy Systemu
def createTableSystemAdmins(cur, db):
    """Funkcja Tworząca tabelę AdministratorzySystemu
    AdministartorID - klucz główny
    AdresID - klucz obcy do tabeli KlienciAdresy
    -------------------------------------------
    """

    #cur.execute("DROP TABLE IF EXISTS AdministratorzySystemu")

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS AdministatorzySystemu(
            AdministatorID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
            KlientID INTEGER NOT NULL REFERENCES Klienci(KlientID),
             --
             Imie  VARCHAR(30),
             Nazwisko  VARCHAR(30),
             Stanowisko VARCHAR(45),
             Telefon VARCHAR(9)

              );"""

    cur.execute(sql)
    return cur, db

#Klienci----------------------------------------------------------
def createTableClients(cur, db):
    """Funkcja Tworząca tabelę Klienci
    KlientID - klucz główny
    -------------------------------------------
    Imie
    Nazwisko
    NazwaFirmy
    """

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS Klienci (
            KlientID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             --
             Imie  CHAR(30),
             Nazwisko  CHAR(30),
             NazwaFirmy CHAR(30)
              );
            """

    cur.execute(sql)
    return cur, db

#KlienciAdresy-------------------------------------------------------
def createTableClientsAdress(cur, db):
    """Funkcja Tworząca tabelę KlienciAdres
    AdresID - klucz główny
    KlientID - klucz obcy do tabeli Klienci
    -------------------------------------------
    Adres
    Miejscowosc
    KodPocztowy
    """

    # Drop table if it already exist using execute() method.
    #cur.execute("DROP TABLE IF EXISTS KlienciAdres")


    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS KlienciAdresy (
             AdresID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             KlientID INTEGER NOT NULL REFERENCES Klienci(KlientID),
             --
             Adres CHAR(30) NOT NULL,
             Miejscowosc  CHAR(30) NOT NULL,
             KodPocztowy  CHAR(6) NOT NULL
              )"""

    cur.execute(sql)
    return cur, db

#KlienciKontakty-------------------------------------------------------
def createTableClientsConstacts(cur, db):
    """Funkcja Tworząca tabelę KlienciKontakty
    KontaktID - klucz główny
    AdresID - klucz obcy z KlienciAdres
    -------------------------------------------
    email
    telefon
    """


    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS KlienciKontakty (
             KontaktID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             AdresID INTEGER NOT NULL REFERENCES KlienciAdres(AdresID),
             --
             email CHAR(40),
             telefon CHAR(9)
              )"""

    cur.execute(sql)
    return cur, db

#-----------------------------------------NMAP--------------------------------
#NmapSkan-----------------------------------
def createTableNmapScan(cur, db):
    """Funkcja Tworząca tabelę SkanNmap
    SkanID - klucz główny
    KlientID - klucz obcy z tabeli Klienci
    -------------------------------------------
    Data
    LiczbaHostowUp
    LiczbaHostowWSieci
    #może Typ - wewnętrzny/zewnętrzny
    """

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS SkanNmap (
             SkanID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             KlientID INTEGER NOT NULL REFERENCES Klienci(KlientID),


             Data DATE,
             LiczbaHostowUp INT,
             LiczbaHostowWSieci INT
              )"""

    cur.execute(sql)
    return cur, db

#Hosty--------------------------------------
def createTableHosts(cur, db):
    """Funkcja Tworząca tabelę Hosty
    HostID - klucz główny
    SkanID - klucz obcy z tabeli SkanNmap
    -------------------------------------------
    HostIP
    MAC
    PortUsluga
    """

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS Hosty (
             HostID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             SkanID INTEGER NOT NULL REFERENCES SkanNmap(SkanID),
             --
             HostIP VARCHAR(16),
             MAC VARCHAR(12),
             PortUsluga VARCHAR(5)

              )"""

    cur.execute(sql)

    return cur, db

# Usługi--------------------------------------
def createTableServices(cur, db):
    """Funkcja Tworząca tabelę Usługi
    UslugaID - klucz główny
    HostID - klucz obcy z tabeli Hosty
    -------------------------------------------
    NazwaUslugi
    """

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS Uslugi (
             UslugaID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             HostID INTEGER NOT NULL REFERENCES Hosty(HostID),

             NazwaUslugi VARCHAR(45),
             OpisUslug MEDIUMTEXT
              )"""

    cur.execute(sql)

    return cur, db

# Zagrozenia--------------------------------------
def createTableVulnerabilities(cur, db):
    """Funkcja Tworząca tabelę Zagrożenia
    ZagrozenieID - klucz główny
    UslugaID - klucz obcy z tabeli uslugi
    -------------------------------------------
    NazwaZagrożenia
    StopienCVE
    KodCVE
    OpisPolski
    OpisAgielski
    """

    # Create table as per requirement
    sql = """CREATE TABLE IF NOT EXISTS Zagrozenia (
             ZagrozenieID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
             UslugaID INTEGER NOT NULL REFERENCES Uslugi(UslugaID),

             NazwaZagrozenia VARCHAR(45),
             StopienCVE VARCHAR(3),
             KodCVE VARCHAR(8),
             IdCVE VARCHAR(3) ,
             OpisAngielski MEDIUMTEXT,
             OpisPolski MEDIUMTEXT
              )"""

    cur.execute(sql)
    return cur, db

#-------------------------------------------------------------------------------------------------------
#--Dodawnie klucz obcych - RElacje między tabelami

def createTableRelations(cur):

    sql = """ALTER TABLE  AdministatorzySystemu ADD FOREIGN KEY(KlientID) REFERENCES Klienci(KlientID);"""
    cur.execute(sql)

    sql = """ALTER TABLE  KlienciAdresy ADD FOREIGN KEY(KlientID) REFERENCES Klienci(KlientID);"""
    cur.execute(sql)

    sql = """ALTER TABLE  KlienciKontakty ADD FOREIGN KEY(AdresID) REFERENCES KlienciAdresy(AdresID);"""
    cur.execute(sql)

    sql = """ALTER TABLE  SkanNmap ADD FOREIGN KEY(KlientID) REFERENCES Klienci(KlientID);"""
    cur.execute(sql)

    sql = """ALTER TABLE Hosty ADD FOREIGN KEY(SkanID) REFERENCES SkanNmap(SkanID);"""
    cur.execute(sql)

    sql = """ALTER TABLE Uslugi ADD FOREIGN KEY(HostID) REFERENCES Hosty(HostID);"""
    cur.execute(sql)

    sql = """ALTER TABLE Zagrozenia ADD FOREIGN KEY(UslugaID) REFERENCES Uslugi(UslugaID) ;"""
    cur.execute(sql)

#--------------------------------------------------------- Dodawanie Danych -------------------------------------------
#dodawanie Nowego klienta----------------------------------------------------------
def addClientToTableClients(cur, db, imie, nazwisko, nazwFirmy):
    """
    Funkcja Dodająca Klienta do bazy danych - tabela Klienci
    wymagane parametry: kursorSQL, bazaDanych, KlientID, AdresID, SkanID, Imie, Nazwisko, NazwaFirmy
    """
    dane = str(imie) + ',' + str(nazwisko) + ',' + str(nazwFirmy)
    KlientID = ''

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Klienci
             VALUES ("""+dane+ ");"


    executeSQLCommand(cur, db, sql)

#dodawanie AdresuKlienta ------------------------------------------
def addClientAddressToTableClientsAddress(cur, db, adres, miejscowosc, kodPocztowy):
    """
    Funkcja Dodająca Adresy Klienta do bazy danych - tabela KlienciAdresy
    wymagane parametry: kursorSQL, bazaDanych, AdresID, KontaktID,  Adres, Miejscowosc , KodPocztowy
    """

    dane = str(adres) + ',' + str(miejscowosc) + ',' + str(kodPocztowy)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO KlienciAdresy(Adres,
             Miejscowosc, KodPocztowy)
             VALUES ("""+dane+ ")"

    executeSQLCommand(cur, db, sql)

#dodawanie KontaktuKlienta ------------------------------------------
def addClientContactToTableClientsContacts(cur, db, email, telefon):
    """
    Funkcja Dodająca Kontakty Klienta do bazy danych - tabela KlienciKontakty
    wymagane parametry: kursorSQL, bazaDanych, KontaktID,  email, telefon
    """
    dane = str(email) + ',' + str(telefon)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO KlienciKontakty(
             Email, Telefon)
             VALUES ("""+dane+ ")"

    executeSQLCommand(cur, db, sql)

#dodawanie skanu do NmapSkan ------------------------------------------
def addScanToNmapScan(cur, db, data, liczbaHostowUp, liczbaHostowWSieci):
    """
    Funkcja Dodająca Dane Skanu do bazy danych - tabela SkanNmap
    wymagane parametry: kursorSQL, bazaDanych, SkanID, HostID , Data, Godzina, LiczbaHostowUP, LiczbaHostowWSieci
    """

    dane = str(data) + ',' + str(liczbaHostowUp) +',' +  str(liczbaHostowWSieci)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO SkanNmap(
             Data, LiczbaHostowUp, LiczbaHostowWSieci)
             VALUES ("""+dane+ ");"


    executeSQLCommand(cur, db, sql)

#dodawanie hosta do Hosty ------------------------------------------
def addHostToHosts(cur, db):
    """
    Funkcja Dodająca Dane Skanu do bazy danych - tabela Hosty
    wymagane parametry: kursorSQL, bazaDanych, HostID , UsługaID, HostIP
    """

    dane = str(HotIP) + ',' + str(MAC) + ',' + str(PortUsluga)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Hosty(
             HostIP, MAC,PortUsluga)
             VALUES ("""+dane+ ");"


    executeSQLCommand(cur, db, sql)

#dodawanie uslugi do Uslugi ------------------------------------------
def addServiceToServices(cur, db, nazwaUslugi, opisUslugi):
    """
    Funkcja Dodająca Dane Skanu do bazy danych - tabela Uslugi
    wymagane parametry: kursorSQL, bazaDanych, UslugaID , ZagrozenieID, NazwaZagrozenia
    """

    dane = str(nazwaUslugi) + ',' + str(opisUslugi)

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Uslugi(
             NazwaUslugi, OpisUslugi)
             VALUES ("""+dane+ ")"

    executeSQLCommand(cur, db, sql)

#dodawanie zagrożenia do Zagrożeń ------------------------------------------
def addVulnerabilityToVulnerabilities(cur, db, stopienCVE, kodCVE, idCVE, opisAngielski, opisPolski):
    """
    Funkcja Dodająca Zagrożenia do bazy danych - tabela Zagrozenia
    wymagane parametry: kursorSQL, bazaDanych, ZagrozeniaID , NazwaZagrozenia, StopienCVE, KodCVE, opisPolski, opisAngielski
    """

    dane = (str(stopienCVE) + ',' + str(kodCVE) + ',' +
            str(idCVe) + ',' + str(opisAngielski) + ',' + str(opisPolski))

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO Zagrozenia(
             NazwaZagrozenia, StopienCVE, KodCVE, IdCVE, OpisAngielski, OpisPolski)
             VALUES ("""+dane+ ")"

    executeSQLCommand(cur, db, sql)

def executeSQLCommand(cur,db, sql):
    try:
        # Execute the SQL command
        cur.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    #db.close()

#---------------------------------------------------MAIN-------------------------------------------------------
def createClientsTables(name, cur, db):
    #----Tworzenie Tabel
    #Klient

    cur, db = createTableClients(cur, db)
    cur, db = createTableSystemAdmins(cur, db)
    cur, db = createTableClientsAdress(cur, db)
    cur, db = createTableClientsConstacts(cur, db)

    return cur, db

def createNmapTables(name, cur, db):
    #Nmap
    cur, db = createTableNmapScan(cur, db)
    cur, db = createTableHosts(cur, db)
    cur, db = createTableServices(cur, db)
    cur, db = createTableVulnerabilities(cur, db)

    return cur, db


#------------------------------------------------------------------------------------------------
listOfBlocks, data, godzina, hostUp, liczbaHostowWSieci = main2.main()

print data
print godzina
print hostUp
print liczbaHostowWSieci

def writeBlocks(listOfBlocks):
    for i in listOfBlocks:
        print i.ip

        # print i.portsList, i.name, i.latency, i.portsList, i.portFunction, i.device, i.system , i.portInformacje
        # writeBlocks(listOfBlocks)


def createTestTable(cur, db):
    sql = """
            CREATE TABLE innodb_parentTest
        (
         iparent_id INT NOT NULL,
         PRIMARY KEY (iparent_id),
         wartosc VARCHAR(30)
        ) ENGINE=INNODB;

        CREATE TABLE innodb_childTest
        (
         iparent_id INT NOT NULL,
         ichild_id INT NOT NULL,
         PRIMARY KEY (iparent_id, ichild_id),
         FOREIGN KEY (iparent_id) REFERENCES innodb_parent (iparent_id),
         wartosc VARCHAR(30)
        ) ENGINE = INNODB;
            """
    executeSQLCommand(cur, db, sql)

    sql = """INSERT INTO innodb_childTest
     VALUES ('WartoscDziecko');"""

    executeSQLCommand(cur, db, sql)

    sql = """INSERT INTO innodb_parentTest
     VALUES ('WartoscRodzic');"""
    executeSQLCommand(cur, db, sql)

def main():
    name = "DataBaseDB"
    cur, db = connectToDatabase(name)
    cur, db = createClientsTables(name, cur, db)
    cur, db = createNmapTables(name, cur, db)
    createTableRelations(cur)

    #----Dodawanie Danych

    #return cur, db
    db.close()

if __name__ == "__main__":
    main()
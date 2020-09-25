"""
SQLITE3 DATA TYPES

# Dynamic Type System
- Integer
- Real
- Text
- Blob
- Numeric

SQLITE3 DATA TYPE CONVERSION
- Integer: INT, INTEGER, TINYINT, SMALLINT, ...
- Real: REAL, DOUBLE, FLOAT, ...
- Text: VARCHAR, CHARACTER, TEXT, ...
- Blob: BLOB
- Numeric: DECIMAL, BOOL, DATE, ...

"""

"""
Sqlite
Pobrać ze strony: https://sqlite.org/download.html

Na windowsa:
sqlite-dll-win64-x64-3330000.zip
sqlite-tools-win32-x86-3330000.zip

Zrobić folder:
c:\sqlite
z cmd:
cd c:\

md sqlite
Wypakować wszystkie pliki (bez zagnieżdżeń z folderów)

Dodać do ścieżki Windowsa:
c:\sqlite


------------------ konsola ------------------
# sprawdzanie czy działa
sqlite3

# utworzenie folderu
md sqlite3
cd sqlite3

# utworzenie bazy
sqlite3 student.db

# tworzenie tabeli
CREATE TABLE sex(
    id TEXT PRIMARY KEY NOT NULL,
    sex_type INTEGER
);

#dodawanie danych
INSERT INTO sex(id, sex_type) VALUES ('M', 1);
INSERT INTO sex(id, sex_type) VALUES ('F', 2);

# włączanie ładnego trybu
.mode column
.header on
SELECT * FROM sex;

#wyswietli sobie
id  sex_type
--  --------
M   1
F   2

# zmiana szerokosci
.widt 15 20
# wyswietla
.schema sex

# tworzenie kolejnej tabeli
CREATE TABLE student(
f_name VARCHAR(23) NOT NULL,
l_name VARCHAR(23) NOT NULL,
sex CHARACTER(1) NOT NULL,
id INTEGER PRIMARY KEY AUTOINCREMENT,
FOREIGN KEY(sex) REFERENCES sex(id)
);

CREATE TABLE test_type(
id INTEGER PRIMARY KEY NOT NULL,
type TEXT NOT NULL
);

CREATE TABLE test(
date DATE NOT NULL,
test_type INT NOT NULL,
id INTEGER PRIMARY KEY AUTOINCREMENT,
FOREIGN KEY (test_type) REFERENCES test_type(id)
);

# tworzenie tabeli z mieszanym id z dwóch idików
CREATE TABLE test_score(
student_id INTEGER NOT NULL,
test_id IINTEGER NOT NULL,
score INTEGER NOT NULL,
FOREIGN KEY (test_id) REFERENCES test(id),
FOREIGN KEY (student_id) REFERENCES student(id),
PRIMARY KEY (test_id, student_id)
);

# stworzenie tabeli nieobecnosci
CREATE TABLE absence(
date DATE NOT NULL,
PRIMARY KEY (student_id, date),
FOREIGN KEY (student_id) REFERENCES student(id)
)l

#wyswietalnie nazw wszystkich tabel jakie mamy
.tables

#wyjscie z konsoli bazy
.exit

"""
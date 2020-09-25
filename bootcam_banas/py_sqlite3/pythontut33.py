"""
wejs do folderu z bazą dancyh
z konsoli
sqlite3 student.db

#########
SELECT student_id, score, test_type, date
FROM test, test_score
WHERE date = '2018-10-1'
AND test.id = test_score.test_id;


#########
SELECT f_name, l_name, score, test_type, date
FROM test, test_score, student
WHERE date = '2018-10-1'
AND test.id = test_score.test_id
AND test_score.student_id = student.id;

sqlite> .header on
sqlite> .mode column


######### zliczanie i group by
# group by - agregate
# formatowanie outputu f_name || ' ' || l_name imie<spacja>nazwisko jako jedna kolumna
# AS aias na kolumnę
SELECT f_name || ' ' || l_name AS Name,
COUNT(absence.date) AS Absences
FROM student, absence
WHERE absence.student_id = student.id
GROUP BY id;


################# inner join - najpopularniejszy typ join
# wyswietla punkty z testow w ktroych brali udzial studenci
# student_id to id z tabeli test_score
# id to kolumna id z tabeli student
SELECT f_name || ' ' || l_name AS Name, score, test_id
FROM test_score JOIN student
ON student_id = id;


################### left join
# wszystkie dane dla lewej cześc/lewej tabeli join
# np. wyświetli wszystkie nieobecnosci studentów, nawet jeśli nie mają żadnej nieobecnosci
SELECT f_name || ' ' || l_name AS Name,
COUNT(absence.date) AS Absence
FROM student LEFT JOIN absence
ON absence.student_id = student.id
GROUP BY id;


############# NATURAL JOIN
# podobny do lewego joina
## Ze złączeniem naturalnym mamy do czynienia, gdy obie kolumny występujące
## w warunku łączącym są tej samej nazwy.
## W przypadku tego typu złączenia możemy stosować jedną z
## czterech możliwych notacji.
## Najczęściej polecaną notacją jest JOIN ... USING,
## zaś najbardziej odradzaną jest notacja „NATURAL JOIN”
## gdyż może się trafić sytuacja gdy będzie więcej dopasowań kolumn
## o tej samej nazwie niż jedna.
## Wówczas efekt jest nieokreślony (co w praktyce oznacza że każdy dostawca baz
## danych ma swój własny tajny sposób poradzenia sobie z tym problemem).

SELECT score, test_id
FROM student NATURAL JOIN test_score
WHERE student_id = id;


############### CROSS JOIN - złączenie kartezjańskie
# raczej unikane, dane wyjściowe są nieuporządkowane
SELECT score, test_id
FROM student CROSS JOIN test_score;

"""

"""
#obliczenia
sqlite> SELECT (1+2) /(6-3) * 10;
(1+2) /(6-3) * 10
-----------------
10


sqlite> SELECT 15 % 10;
15 % 10
-------
5

#opercje boolowskie 0 - false ; liczby różne od 0 to True
sqlite> SELECT 1 AND 0 , 1 OR 0, NOT 1;
1 AND 0  1 OR 0  NOT 1
-------  ------  -----
0        1       0

# sprawdzanie IN danych w liście, cudzyslow albo pojedyncze ciapki przy stringach
sqlite> SELECT 'Paul' IN ("Mike", "Paul");
'Paul' IN ('Mike', 'Paul')
--------------------------
1

# BETWEEN do porównywanie między
sqlite> SELECT * FROM test_score
   ...> WHERE score
   ...> BETWEEN 15 and 20;
student_id  test_id  score
----------  -------  -----
6           1        18
9           1        20
5           2        18
6           2        16
9           2        17
7           3        17
2           4        19
9           4        15

## pobieranie min i max
sqlite> SELECT min(id), max(id)
   ...> FROM student;
min(id)  max(id)
-------  -------
1        10

### pobieranie LICZBY ZMIAN na BAZIE - dane bazy danych
sqlite> SELECT total_changes();
total_changes()
---------------
61
"""
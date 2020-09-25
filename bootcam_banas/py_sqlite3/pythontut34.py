"""
wejść do folderu z baza dancyh
z konsoli
sqlite3
"""

"""
#najlepszy i najgroszy wynik
sqlite> SELECT test.date AS Date,
   ...> MIN(test_score.score) AS Worst,
   ...> MAX(test_score.score) AS Best
   ...> FROM test_score, test
   ...> WHERE test_score.test_id = test.id
   ...> GROUP BY test.date;
Date       Worst  Best
---------  -----  ----
2018-10-1  -1     20
2018-10-2  4      24
2018-10-4  2      24

"""

"""
#srednia wynikow z testu
# ciapki jak nazwa aliasu ze spacją 
sqlite> SELECT test.date AS Date,
   ...> AVG(test_score.score) 'Avg Score'
   ...> FROM test_score, test
   ...> WHERE test_score.test_id = test.id
   ...> GROUP BY test.date;
Date       Avg Score
---------  ---------
2018-10-1  7.9
2018-10-2  12.9
2018-10-4  14.05
"""

"""
# lista studentow z wynikiem powyzej 20
SELECT f_name || ' ' || l_name AS Name,
test_score.score AS Score
FROM test_score, student
WHERE test_score.score > 20
AND test_score.student_id = student.id
GROUP BY Name;
"""


################## Views ##################

"""
CREATE VIEW ScoreOver21 AS
SELECT f_name || ' ' || l_name AS Name,
test_score.score
FROM test_score, student
WHERE test_score.score > 21
AND test_score.student_id = student.id
GROUP BY Name;


sqlite> SELECT * FROM ScoreOver21;
Name               score
-----------------  -----
Jackson Jackson    24
Taylor Taylor      24
Thompson Thompson  22
White White        22

# usuwanie widoku
DROP VIEW ScoreOver21;

"""

################### TRIGGERS  ###################
"""
CREATE TABLE log(
id INT PRIMARY KEY,
test_id INT NOT NULL,
date DATE NOT NULL,
student_id INT NOT NULL,
FOREIGN KEY (test_id) REFERENCES test_score(test_id),
FOREIGN KEY (student_id) REFERENCES test_score(student_id)
);


CREATE TRIGGER test_score_update
AFTER UPDATE OF score ON test_score
BEGIN
INSERT INTO log(test_id, date, student_id)
VALUES (new.test_id, date('now'), new.student_id);
END;


sqlite> SELECT * FROM absence;
student_id  date
----------  ---------
1           2018-10-1
2           2018-10-1
3           2018-10-1

#aktualizacja danych w tabeli
UPDATE test_score
SET score = 20
WHERE test_id = 1 AND student_id = 2;

# sprawdzenie tabeli logów, czy trigger zadziałał
sqlite> SELECT * FROM log;
id  test_id  date        student_id
--  -------  ----------  ----------
    1        2020-09-07  2
    
"""

################## lIKE ##################
"""
# % 0 albo więcej liter
SELECT l_name, f_name 
FROM student
WHERE l_name LIKE 'J%';

l_name   f_name
-------  -------
Jackson  Jackson


# nazwisko na pięć liter - podzłoga oznacza lietere albo spacje
SELECT l_name, f_name 
FROM student
WHERE l_name LIKE '______';

l_name  f_name
------  ------
Davis   Davis
White   White


sqlite> SELECT l_name, f_name
   ...> FROM student;
l_name    f_name
--------  --------
Jackson   Jackson
Davis     Davis
Thompson  Thompson
Thompson  Thompson
Thompson  Thompson
Taylor    Taylor
White     White
Taylor    Taylor
Miller    Miller
Anderson  Anderson


#ASC rosnaco, DESC malejąco
# offset 2 - widac od drugiego rekordu WLACZNIE (sql numeruje od 1)
sqlite> SELECT l_name, f_name
   ...> FROM student
   ...> WHERE f_name LIKE 'T%'
   ...> ORDER BY l_name ASC, f_name LIMIT 5 OFFSET 2;
l_name    f_name
--------  --------
Thompson  Thompson
Thompson  Thompson
Thompson  Thompson


sqlite> SELECT l_name, f_name
   ...> FROM student
   ...> WHERE f_name LIKE 'T%'
   ...> ORDER BY l_name ASC, f_name LIMIT 5 OFFSET 1;
l_name    f_name
--------  --------
Taylor    Taylor
Thompson  Thompson
Thompson  Thompson
Thompson  Thompson

"""

# losowe lioczby
"""
SELECT random();

# losowa dodatnia liczba od <0 do 100>
SELECT ABS(RANDOM() % 100);
"""

# zamiana na wielkie litery
"""
SELECT LOWER(f_name),
UPPER(l_name)
FROM student;
LOWER(f_name)  UPPER(l_name)
-------------  -------------
jackson        JACKSON
davis          DAVIS
thompson       THOMPSON
thompson       THOMPSON
thompson       THOMPSON
taylor         TAYLOR
white          WHITE
taylor         TAYLOR
miller         MILLER
anderson       ANDERSON
"""

# dlugosc stringa
"""
SELECT LENGTH('Iron Man');
LENGTH('Iron Man')
------------------
8
"""

"""
SELECT COUNT(*) FROM student;
COUNT(*)
--------
10
"""

# dayty numeruje od 0, 0 to niedziela, 0 to styczen
"""
SELECT date();
date()
----------
2020-09-07


SELECT time();
time()
--------
22:49:03

SELECT datetime();
datetime()
-------------------
2020-09-07 22:49:32

#srawdzanie daty 30 dni temu
SELECT date('now', '-30 days');
date('now', '-30 days')
-----------------------
2020-08-08

# szukanie daty nastepnej niedzieli ( to peirwszy dzien w amerykanskim kalendarzu)
SELECT date('now', 'weekday 0');
date('now', 'weekday 0')
------------------------
2020-09-13


# formatowanie informacji
SELECT strftime("%d-%m-%Y");
strftime("%d-%m-%Y")
--------------------
07-09-2020


#szukanie święta dziękczynienia - są specyficzne warunki a nie konkretna data
SELECT date('now', 'start of year', 
'10 months',  '21 days', 'weekday 4');
-------------------------------------------------------------------
2020-11-26

"""
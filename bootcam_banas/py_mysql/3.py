import mysql.connector
from mysql.connector import Error

"""
Nazwa TABELI - liczba mnoga
Nazwa KOLMNY - liczba pojedyncza
"""

def my_query(query, fetchall=True):
    try:
        conn = mysql.connector.connect(
            host="localhost", database='students', user="studentadmin", password="password"
        )
        cursor = conn.cursor()

        cursor.execute(query)

        if fetchall:
            results = cursor.fetchall()
            return results
        else:
            return None

    except mysql.connector.Error as error:
        print("Error: ", str(error))

    finally:
        if conn.is_connected():
            conn.close()
        print("Database connection closed")


def q_1():
    """
    Min, MAX, SUM, AVG - funkcje SQLa
    GROUP BY
    :return:
    """
    query = 'SELECT test_id, MIN(score), MAX(score), MAX(score) - MIN(score), SUM(score), AVG(score) ' \
            'FROM scores ' \
            'GROUP BY test_id;'

    results = my_query(query)
    for x in results:
        print(x[0], "Min :", x[1], " Max: ", x[2], " Rng: ", x[3], " Sum: ", x[4], " Avg: ", x[5])


def q_2():
    # spr na których testach był student 6
    query = 'SELECT student_id , test_id FROM scores WHERE student_id = 6'

    results = my_query(query)
    for x in results:
        print(x[0], x[1])


def q_3():
    # INSERT, DELETE, WHERE
    # spr na których testach był student 6
    # nie chce insertowac z poziomu pycharm jako user studentadmin; ale jako admin już to robi z Workbencha
    query = 'INSERT INTO scores VALUES (6, 3, 24)' #aktualizacj apunktów - 24pkt  dla testu nr 3
    # SELECT * FROM scores
    my_query(query, fetchall=False)
    #
    query = "DELETE FROM absences WHERE student_id = 6;"
    my_query(query, fetchall=False)

    query = "SELECT student_id, test_id " \
            "FROM scores " \
            "WHERE student_id = 6;"

    results = my_query(query)
    for x in results:
        print(x[0], x[1])


def q_4():
    """
    dodwanie kolumny do tabeli
    :return:
    """
    query = 'ALTER TABLE absences ADD COLUMN test_taken CHAR(1) NOT NULL DEFAULT "F" AFTER student_id'
    my_query(query, fetchall=False)


def q_5():
    """
    MODIFY the column, z char(1) na enuma
    :return:
    """
    query = 'ALTER TABLE absences MODIFY COLUMN test_taken ENUM("T", "F") NOT NULL DEFAULT "F"'
    my_query(query, fetchall=False)


def q_6():
    """
    ALTER TABLE
    :return:
    """
    query = 'ALTER TABLE absences DROP COLUMN test_taken'
    my_query(query, fetchall=False)


def q_7():
    """
    UPDATE konkretnej wartosci
    jak ouzytkownik studentadmin tego nie aktualizuje ;/
    :return:
    """

    # [!]  studentadmin tego nie aktualizuje
    query = 'UPDATE scores SET score= 25 WHERE student_id=4 AND test_id=3'
    my_query(query, fetchall=False)

    query = 'SELECT * FROM scores  WHERE student_id=4 AND test_id=3'
    results = my_query(query)
    for x in results:
        print(x[0], " test_id: ", x[1], " score: ", x[2])


def q_8():
    """
    BETWEEN
    :return:
    """
    query = 'SELECT first_name, last_name, birth_day ' \
            'FROM students ' \
            'WHERE birth_day BETWEEN "1960-1-1" AND "1970-1-1"'

    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2])


def q_9():
    """
    IN
    :return:
    """
    query = 'SELECT first_name, last_name, birth_day ' \
            'FROM students ' \
            'WHERE first_name IN ("Bobby", "Lucy" , "Andy")'

    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2])


def q_10():
    """
    JOIN
    #dobra praktyka - na poczatku nazwa stbeli
    """
    query = 'SELECT scores.student_id, tests.date, scores.score, tests.maxscore FROM tests, scores ' \
            'WHERE date = "2014-08-25" AND tests.test_id = scores.test_id'
    #warunek złączenia

    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2], " ", x[3])


def q_11():
    """
    JOIN 3 tabel, z reugły łączy się po id będących kluczami
    CONCAT
    #dobra praktyka - na poczatku nazwa stbeli tabela.kolumna
    """
    query = 'SELECT CONCAT(' \
            'students.first_name, " ", students.last_name) AS Name, ' \
            'tests.date, scores.score, tests.maxscore ' \
            'FROM tests, scores, students ' \
            'WHERE date="2014-08-25" AND tests.test_id = scores.test_id AND scores.student_id = students.student_id'
    #warunek złączenia

    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2], " ", x[3])


def q_12():
    """
    JOIN 3 tabel, z reugły łączy się po id będących kluczami
    Zliczanie nieobecnosci studenta
    """
    # BEZ GROUP BY - zwraca tylko jednego pierwzego studenta
    query = 'SELECT students.student_id, students.first_name, students.last_name, ' \
            'COUNT(absences.date) ' \
            'FROM students, absences ' \
            'WHERE students.student_id = absences.student_id' #warunek złączenia


    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2], " ", x[3])

    # GROUP BY students.student_id
    #ZWRACA wszystkich studewntów z nieobecnosciami
    query = 'SELECT students.student_id, students.first_name, students.last_name, ' \
            'COUNT(absences.date) ' \
            'FROM students, absences ' \
            'WHERE students.student_id = absences.student_id ' \
            'GROUP BY students.student_id;'

    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2], " ", x[3])


def q_13():
    """
    INNER JOIN, niezbyt często używane
    From tabela_1 INNER JOIN tabela_2 ON tabela_1.id = tabela_2.klucz_obcy_z_tab_1
    """

    query = 'SELECT students.first_name, students.last_name, scores.test_id, scores.score ' \
            'FROM students INNER JOIN scores ON students.student_id = scores.student_id ' \
            'WHERE scores.score <=15 ' \
            'ORDER BY scores.test_id'


    results = my_query(query)
    if results:
        for x in results:
            print(x[0], "", x[1], " ", x[2], " ", x[3])



if __name__ == "__main__":
    # q_1()
    # q_2()
    # q_3()
    # q_4()
    #q_5()
    # q_6()
    # q_7()
    # q_8()
    # q_9()
    # q_10()
    # q_11()
    # q_12()
    q_13()

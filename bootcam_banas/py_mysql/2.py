import mysql.connector
from mysql.connector import Error, errorcode

try:
    conn = mysql.connector.connect(
        host="localhost", database="students", user="studentadmin", password="password"
    )

    # query = "SELECT * FROM students"

    """
    # WHERE
    # query = 'SELECT first_name, last_name ' \
    #         'FROM students ' \
    #         'WHERE state="WA"'
    """

    """
    # YEAR(data_column) funkcja mysql do wyciągadania roku z daty
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'WHERE YEAR(birth_day) >= 1965'
    """

    """
    # WHERE OR
    # MONTH(birth_day) - funkcja mysql
    # 2 to luty
    # CA - stan Kalifornia
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'WHERE MONTH(birth_day) = 2 OR state="CA";'
    """

    """
    # DAY(birth_day) - funkcja mysql
    # AND i && to to samo
    # OR i || to to samo
    query = 'SELECT last_name, state, birth_day ' \
            'FROM students ' \
            'WHERE DAY(birth_day) >= 12 && (' \
            'state="CA" || state="NV" \
            );'

    """

    """
    #  IS NOT NULL
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'WHERE last_name IS NOT NULL;'
    """

    """
    # ORDER BY
    # LIMIT 5 - zwraca 5 pierwszych wynikow 1,2,3,4,5
    # LIMIT 5, 10 zwraca 6,7,8,9,10 wyniki
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'ORDER BY last_name LIMIT 5'

    """

    """
    #CONCAT i aliasy
    query = 'SELECT CONCAT(first_name, " ", last_name) AS "Name", ' \
            'CONCAT(city, " ", state) AS "Hometown" ' \
            'FROM students;'
    """

    """
    #LIKE %dowolna liczba znaków
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'WHERE first_name LIKE "D%" OR last_name LIKE "%n"; '
    """

    """
    # LIKE _ dowony jeden znak
    query = 'SELECT first_name, last_name ' \
            'FROM students ' \
            'WHERE first_name LIKE "____y"'
    """

    # GROUP BY i COUNT
    """
    query = 'SELECT sex, COUNT(*)' \
            'FROM students ' \
            'GROUP BY sex'
    """

    """
    # GROUP BY,  COUNT, ORDER BY
    query = 'SELECT MONTH(birth_day) AS "MONTH", ' \
            'COUNT(*) ' \
            'FROM students ' \
            'GROUP BY Month ' \
            'ORDER BY Month'
    """

    """
    # HAVING
    query = 'SELECT state, COUNT(state) AS "Amount" ' \
            'FROM students ' \
            'GROUP BY state ' \
            'HAVING Amount > 1'
    """

    """
    # DISTINCT
    query = 'SELECT DISTINCT state ' \
            'FROM students ' \
            'GROUP BY state '
    """

    """
    # COUNT(DISTINCT)
    query = 'SELECT COUNT(DISTINCT state) FROM students'
    """

    cursor = conn.cursor()
    cursor.execute(query)
    student = cursor.fetchall()
    print("Total number of results: ", len(student))
    for s in student:
        # print(s[0], " ", s[1])
        print(s[0])

except mysql.connector.Error as error:
    print("Error: ", error)

finally:
    if conn.is_connected():
        conn.close()
    print("Connection to database closed")
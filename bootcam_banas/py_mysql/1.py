import mysql.connector
from mysql.connector import Error, errorcode
from datetime import datetime

"""
CREATE TABLE class(
name VARCHAR(45) NOT NULL,
class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE test(
date DATE NOT NULL,
type ENUM('T', 'Q') NOT NULL,
class_id INT UNSIGNED NOT NULL,
test_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE score(
student_id INT UNSIGNED NOT NULL,
event_id INT UNSIGNED NOT NULL,
score INT NOT NULL,
PRIMARY KEY(event_id, student_id)
);

CREATE TABLE absence(
student_id INT UNSIGNED NOT NULL,
date DATE NOT NULL,
PRIMARY KEY(student_id, date)
);

ALTER TABLE test ADD maxscore INT NOT NULL AFTER type;

ALTER TABLE score CHANGE event_id test_id INT UNSIGNED NOT NULL;

RENAME TABLE
absence TO absences,
class TO classes,
score TO scores,
student TO students,
test TO tests;

"""

try:
    conn = mysql.connector.connect(
        host="localhost", database="students", user="studentadmin", password="password"
    )

    """
    #dodawanie jednego wiersza wartosci
    # query = "INSERT INTO students VALUES " \
    #         "(NULL, 'Dale', 'Cooper', 'dcooper@aol.com', '123 Main St', 'Yakima', " \
    #         "'WA', 98901, '792-223-8901', '1952-2-22', 'M', NOW(), 3.50)"
    
    # cursor.execute(query) #dodwanei jednego wiersza
    SELECT * FROM students;

    """
    """
    # dodawanie wiele wierszy danych
    query = "INSERT INTO students (student_id, first_name, last_name, email, street, city, state, zip, phone, " \
            "birth_day, sex, date_entered, lunch_cost) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


    now_time = datetime.now()
    format_date = now_time.strftime("%Y-%m-%d %H:%M:%S")
    students = [(None, 'Harry', 'Truman', 'htruman@aol.com', '202 South St', 'Vancouver', 'WA', 98660, '792-223-9810', '1946-1-24','M', format_date, 3.50),
    (None, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431, '792-223-6734', '1970-12-12','F', format_date, 3.50),
    (None, 'Bobby', 'Briggs', 'bbriggs@aol.com', '14 12th St', 'San Diego', 'CA',92101, '792-223-6178', '1967-5-24','M', format_date, 3.50),
    (None, 'Donna', 'Hayward', 'dhayward@aol.com', '120 16th St', 'Davenport', 'IA', 52801, '792-223-2001', '1970-3-24','F', format_date, 3.50),
    (None, 'Audrey', 'Horne', 'ahorne@aol.com', '342 19th St', 'Detroit', 'MI', 48222, '792-223-2001', '1965-2-1','F', format_date, 3.50),
    (None, 'James', 'Hurley', 'jhurley@aol.com', '2578 Cliff St', 'Queens', 'NY', 11427, '792-223-1890', '1967-1-2','M', format_date, 3.50),
    (None, 'Lucy', 'Moran', 'lmoran@aol.com', '178 Dover St', 'Hollywood', 'CA', 90078, '792-223-9678', '1954-11-27','F', format_date, 3.50),
    (None, 'Tommy', 'Hill', 'thill@aol.com', '672 High Plains', 'Tucson', 'AZ', 85701, '792-223-1115', '1951-12-21','M', format_date, 3.50),
    (None, 'Andy', 'Brennan', 'abrennan@aol.com', '281 4th St', 'Jacksonville', 'NC', 28540, '792-223-8902', '1960-12-27','M', format_date, 3.50)]
    
    SELECT * FROM students;
    # cursor.executemany(query, students) #dodawanie wielu wierszy
    """

    """"
    # 3. Insert multiple rows with one query
    query = "INSERT INTO classes VALUES ('English', NULL), ('Speech', NULL), ('Literature', NULL),('Algebra', NULL), " \
            "('Geometry', NULL), ('Trigonometry', NULL), ('Calculus', NULL), ('Earth Science', NULL), " \
            "('Biology', NULL), ('Chemistry', NULL), ('Physics', NULL), ('History', NULL),('Art', NULL), ('Gym', NULL);"

    # cursor.execute(query)
    # SELECT * FROM classes;
    """

    """
    # 4. Enter test data
    query = "INSERT INTO tests VALUES ('2014-8-25', 'Q', 15, 1, NULL), ('2014-8-27', 'Q', 15, 1, NULL), " \
            "('2014-8-29', 'T', 30, 1, NULL), ('2014-8-29', 'T', 30, 2, NULL), ('2014-8-27', 'Q', 15, 4, NULL), " \
            "('2014-8-29', 'T', 30, 4, NULL)"

    # cursor.execute(query) #dodwanei jednego wiersza
    # SELECT * FROM tests;
    """

    """
    # 5. Insert score data
    query = "INSERT INTO scores VALUES (1, 1, 15),(1, 2, 14),(1, 3, 28),(1, 4, 29),(1, 5, 15),(1, 6, 27),(2, 1, 15)," \
            "(2, 2, 14),(2, 3, 26),(2, 4, 28),(2, 5, 14),(2, 6, 26),(3, 1, 14),(3, 2, 14),(3, 3, 26),(3, 4, 26)," \
            "(3, 5, 13),(3, 6, 26),(4, 1, 15),(4, 2, 14),(4, 3, 27),(4, 4, 27),(4, 5, 15),(4, 6, 27),(5, 1, 14)," \
            "(5, 2, 13),(5, 3, 26),(5, 4, 27),(5, 5, 13),(5, 6, 27),(6, 1, 13),(6, 2, 13),(6, 4, 26),(6, 5, 13)," \
            "(6, 6, 26),(7, 1, 13),(7, 2, 13),(7, 3, 25),(7, 4, 27),(7, 5, 13),(8, 1, 14),(8, 3, 26),(8, 4, 23)," \
            "(8, 5, 12),(8, 6, 24),(9, 1, 15),(9, 2, 13),(9, 3, 28),(9, 4, 27),(9, 5, 14),(9, 6, 27),(10, 1, 15)," \
            "(10, 2, 13),(10, 3, 26),(10, 4, 27),(10, 5, 12),(10, 6, 22)"
    SELECT * FROM scores;
    cursor.execute(query)
    """

    """
    # 6. Insert absences
    query = "INSERT INTO absences VALUES (6, '2014-08-29'),(7, '2014-08-29'),(8, '2014-08-27')"
    SELECT * FROM absences;
    cursor.execute(query)
    """

    cursor = conn.cursor()
    # cursor.execute(query) #dodwanei jednego wiersza
    # cursor.executemany(query, students) #dodawanie wielu wierszy
    cursor.execute(query)

    conn.commit()
    print("Data Entered")
    cursor.close()

except mysql.connector.Error as error:
    print("Error: ", str(error))

finally:
    if conn.is_connected():
        conn.close()
        print("Database Connection Closed")
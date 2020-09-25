"""
w konsli
wejść do folderu z bazą
sqlite3 student.db
.schema student
# wyswietla schemat utworzenia tabeli

#dodawanie daty aktualnej
INSERT INTO test VALUES (date('now'), 1, NULL);

"""

import random
f_names = ["Michael", "Christopher", "Joshua", "Matthew", "David",
           "Daniel", "Andrew", "Joseph", "Justin", "James",
           "Jessica", "Ashley", "Brittany", "Amanda", "Melissa",
           "Stephanie", "Jennifer", "Samantha", "Sarah", "Megan", "Lauren"]
l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
           "Davis", "Miller", "Wilson", "Moore", "Taylor",
           "Anderson", "Thomas", "Jackson", "White", "Harris",
           "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]


def create_students(how_many):
    for i in range(how_many):
        f_name = f_names[random.randint(0, len(f_names) - 1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]

        sex = random.choice(["M", "F"])
        print(f"INSERT INTO student (f_name, l_name, sex) VALUES('{l_name}', '{l_name}', '{sex}');")


#create_students(10)


def create_test_scores(num_tests, num_studs):
    """
    sqlite> .schema test_score
    CREATE TABLE test_score(
    student_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (test_id) REFERENCES test(id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    PRIMARY KEY (test_id, student_id));
    """
    for i in range(1, num_tests + 1):
        for j in range(1, num_studs + 1):
            score = random.randrange(1, 25)
            print(f"INSERT INTO test_score VALUES ({j}, {i}, {score});")


create_test_scores(4, 10)
# sqlite> .mode column
# sqlite> .header on
# sqlite> SELECT * FROM  test_score;
# student_id  test_id  score

"""
sqlite> .schema test_score
CREATE TABLE test_score(
student_id INTEGER NOT NULL,
test_id INTEGER NOT NULL,
score INTEGER NOT NULL,
FOREIGN KEY (test_id) REFERENCES test(id),
FOREIGN KEY (student_id) REFERENCES student(id),
PRIMARY KEY (test_id, student_id));
"""

# UPDATE test_score
# SET score = -1
# WHERE student_id = 1 AND test_id = 1;
#
# UPDATE test_score
# SET score = -1
# WHERE student_id = 2 AND test_id = 1;
#
# UPDATE test_score
# SET score = -1
# WHERE student_id = 3 AND test_id = 1;



# .schema absence
# INSERT INTO absence
# VALUES(1, '2018-10-1');
#
# INSERT INTO absence
# VALUES(2, '2018-10-1');
#
# INSERT INTO absence
# VALUES(3, '2018-10-1');
#
# SELECT * FROM absence;
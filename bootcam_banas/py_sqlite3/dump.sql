BEGIN TRANSACTION;
CREATE TABLE employees (                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,                    f_name TEXT NOT NULL,                     l_name TEXT NOT NULL,                    age INT NOT NULL,                    address TEXT,                    salary REAL,                    hire_date TEXT                    , 'image' BLOB DEFAULT NULL);
INSERT INTO "employees" VALUES(2,'Derek','Banas',43,'123 Main St',500000.0,'2020-09-12',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('employees',2);
COMMIT;

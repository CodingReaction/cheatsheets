COLUMN: attributes of the table (sex, name, etc)
ROWS  : a group of specific attributes for an entry.
DEGREE: number of attributes of a table
CARDINALITY: number of rows

########################## ATOMIC
"when the data is broken in the smallest pieces and can''t be further divided"

Making the info of the table atomic (data is accurate, table is efficient)
Making the table easy to query (short and to the point)

RULE 1: NO multiple values of same type in column. ex COLUMN drinks with ROW value 'alcohol, coca cola, water'
RULE 2: NO multiple columns with same type of data. ex COLUMNs teacher, student1, studen2, student2, etc

NORMAL table = it follows certain rules
+ Won''t have dups so size is less
+ Less data = faster queries

1st NORMAL FORM:
-- Row is ATOMIC
-- Row is UNIQUE (PK)


#################### CLI

\l 	    # list all databases
\c DB_NAME  # connecto DB_NAME [ USE DB_NAME ]
\d my_table # show attrbs of my_table [ DESC my_table ]

\TODO: # show table structure [SHOW CREATE TABLE my_table]

# NULL
-Not the same as 0 or ''
-Not equal to another NULL

################### BASICS

CREATE DATABASE School;
CREATE TABLE students {
	name VARCHAR(20) NOT NULL,
	inscription DATE,
	age INT,
	gender CHAR(1), # M, F, B
	family_description TEXT,
	last_time_sick DATETIME,
	launch_money DEC(5, 2) DEFAULT 11.2,
	PRIMARY KEY (my_id)
);

DROP TABLE students;

INSERT INTO students (name, age, birthday) VALUES ('Max', 40, '1990-10-10'); # only listed values
INSERT INTO students VALUES (....); # all values in order of table declaration

SELECT * FROM students WHERE name='Max' AND inscription IS NULL;
SELECT name, inscription FROM students; # 'Max' | '1997-03-02'

DELETE FROM students WHERE name='Max';

UPDATE students SET age=34, launch_money=0.0 WHERE name='Max';

##################### TEXT SEARCHING: LIKE

WHERE name LIKE '%is'; # % = finished with 'is'

%STRING = multiple chars previously, finished with STRING [can also be STRING%]
_STRING = one char previously, finished with STRING [can also be STRING_]

##################### >= AND <=: BETWEEN

SELECT name FROM students WHERE AGE BETWEEN 18 AND 22;

#################### OR OR OR: IN (..,..,..)

SELECT name FROM students WHERE gender IN ('M', 'F', 'O'); # also [NOT IN]


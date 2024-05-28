-- # Foreign Key Constraint

CREATE TABLE student
(
student_id INT AUTO_INCREMENT,
student_fname VARCHAR(30) NOT NULL,
student_lname VARCHAR(30) NOT NULL,
student_mname VARCHAR(30),
student_email VARCHAR(30) NOT NULL,
student_phone VARCHAR(15) NOT NULL,
student_alternate_phone VARCHAR(15),
enrollment_date TIMESTAMP NOT NULL,
selected_course INT NOT NULL DEFAULT 1,
years_of_exp INT NOT NULL,
student_company VARCHAR(30),
batch_date VARCHAR(30) NOT NULL,
source_of_joining VARCHAR(30) NOT NULL,
location VARCHAR(30) NOT NULL,
PRIMARY KEY(student_id),
UNIQUE KEY(student_email),
FOREIGN KEY(selected_course) REFERENCES courses(course_id)
);
﻿

-- create courses table 
CREATE TABLE courses
(
course_id INT NOT NULL,
course_name VARCHAR(50) NOT NULL,
course_duration_months INT NOT NULL,
course_fee INT NOT NULL,
PRIMARY KEY(course_id)
);


-- parent - courses
-- child - students


-- if data inserted into student student_course which is foreign key, it will check if that student_course integer number will match to the course_id otherwise it will show an error


-- the foreign key is constraint is used to prevent actions that would destroy links between two tables

-- a foregin key is a field in one table that refers to the primary key in another table

-- selected course is a foreign key in students table which refers to course_id (primary key) in courses table

-- the table with the foreign key is called the child table, the table with primary key is called the parent or referenced


-- =========
-- constraints are used to limit the type of data that can ho into a table
-- This ensures the accuracy and reliability of the data is maintaineed
-- if there is any violation then the action is aborted




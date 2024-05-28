CREATE TABLE courses_new(
course_id INT NOT NULL,
course_name VARCHAR(30) NOT NULL,
course_duration_months DECIMAL(3,1) NOT NULL,  -- (3,1) means that it should have max 3 numbers and 1 number after point, Like - 12.5, 3.5
course_fee INT NOT NULL,
changed_at TIMESTAMP DEFAULT NOW() ON UPDATE NOW(), -- This will record the time of any updation on this table, NOW() or CURRENT_TIMESTAMP() both are same, 
PRIMARY KEY(course_id)
);

INSERT INTO courses_new(course_id, course_name, course_duration_months, course_fee) VALUES(1, 'big_data', 6.5, 50000);

INSERT INTO courses_new(course_id, course_name, course_duration_months, course_fee) VALUES(2, 'web development', 3.5, 20000);

INSERT INTO courses_new(course_id, course_name, course_duration_months, course_fee) VALUES(3, 'data science', 6.0, 40000);

INSERT INTO courses_new(course_id, course_name, course_duration_months, course_fee) VALUES(4, 'devops', 10.5, 80000);

DESC courses_new;

UPDATE courses_new SET course_fee=60000 WHERE course_id=2;
SELECT * FROM courses_new;





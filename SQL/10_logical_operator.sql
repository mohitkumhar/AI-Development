
SELECT * FROM student WHERE location='bangalore';

-- to get student who are not form bangalore
SELECT * FROM student WHERE location!='bangalore';

-- to get courses which has the word 'data'
SELECT * FROM courses WHERE course_name LIKE '%data%'; 

-- to get courses which has not the word 'data'
SELECT * FROM courses WHERE course_name NOT LIKE '%data%'; 

-- all student from bangalore who joined through linkedin and have less then than 8 year of experience
SELECT * FROM student WHERE location='hyderabad' AND selected_course='1' AND years_of_exp < 8;

-- to print who do not fall between 2 to 4 years of experience
SELECT * FROM student WHERE years_of_exp > 4 OR years_of_exp < 2;
-- OR
SELECT * FROM student WHERE years_of_exp NOT BETWEEN 2 and 4;

-- get list of students who are working for google, microsoft or amazon
SELECT * FROM student WHERE student_company='google' OR student_company='microsoft' or student_company='amazon';
-- OR
SELECT * FROM student WHERE student_company IN ('google', 'microsoft', 'amazon');


-- if a course is more than 4 months we categorize it as masters program else it is a diploma
SELECT course_id, course_name, course_fee, 
	CASE
		WHEN  course_duration_months > 4 THEN 'masters'
        ELSE 'diploma'
    END AS course_type
FROM courses;

-- people working for microsoft, google, amazon we want to say product based and all others service based

SELECT student_id, student_fname, student_email, location,
	CASE
		WHEN student_company IN ('amazon', 'microsoft') THEN 'product based'
        WHEN student_company='google' THEN 'googler'
        ELSE 'service based'    
    END AS company_type
FROM student;













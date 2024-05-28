-- aggregate function
-- An aggregate function in SQL combines multiple values into a single result, like finding the sum, average, min, or max.

SELECT COUNT(*) FROM student;

SELECT COUNT(DISTINCT student_company) AS number_of_company FROM student;

SELECT COUNT(batch_date) FROM student WHERE batch_date LIKE '%-05-%'; -- student who join batch in may month

-- GROUP BY
-- what i want is to know that how many people have joined my course git to know about me through

-- like:
-- linkedin - 5
-- google - 2
-- quora - 1

-- source_of_joining
SELECT source_of_joining, COUNT(*) FROM student GROUP BY source_of_joining;

SELECT location, COUNT(*) FROM student GROUP BY location;

SELECT location, source_of_joining, COUNT(*) FROM student GROUP BY location, source_of_joining;

SELECT selected_course, COUNT(*) FROM student GROUP BY selected_course;

SELECT batch_date, selected_course, COUNT(*) FROM student GROUP BY batch_date, selected_course;



-- MIN and MAX
-- ============

-- find the minumum experince of student
SELECT MIN(years_of_exp) FROM student;

-- find the maximum experince of student
SELECT MAX(years_of_exp) FROM student;

SELECT MIN(years_of_exp), student_fname FROM student; -- this will give an error
-- to achieve that result
SELECT student_fname, years_of_exp FROM student ORDER BY years_of_exp LIMIT 1;

-- each souce of joining I want get max experience
SELECT source_of_joining, MAX(years_of_exp) FROM student GROUP BY source_of_joining;

-- SUM
-- ======
SELECT source_of_joining, SUM(years_of_exp) FROM student GROUP BY source_of_joining;


-- AVG
-- =====
SELECT source_of_joining, AVG(years_of_exp) FROM student GROUP BY source_of_joining;

SELECT location, AVG(years_of_exp) FROM student GROUP BY location ORDER BY AVG(years_of_exp) DESC;
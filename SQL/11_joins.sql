-- JOINS

-- 2 tables
-- ==========
-- courses
-- students

-- i want to know in which course dave has enrolled


-- student
-- ============
-- student_fname, selected_course
-- dave, 1

-- courses
-- =========
-- courses_id, course_name
-- 1, big data

SELECT course_name FROM courses WHERE course_id=(SELECT selected_course FROM student WHERE student_fname='dave');


-- to join the table (it will be easy approach then apove query)
-- in student table selected_course
-- in courses table course_id

SELECT student_fname, student_lname, course_name FROM student JOIN courses ON student.selected_course = courses.course_id;
-- OR

-- inner join
-- ================
SELECT student.student_fname, student.student_lname, courses.course_name FROM student JOIN courses ON student.selected_course = courses.course_id;

-- by default it is inner joint
-- only the matching records are considered. Non matching records are discarded



-- left outer join
-- ==================
-- all the matching records from left and right table are considered
-- +
-- all the non matching records in the left table which does not have the match in the right padded with null

CREATE TABLE student_latest AS SELECT * FROM student;
CREATE TABLE courses_latest AS SELECT *	 FROM courses;

SELECT student_latest.student_fname, student_latest.student_lname, courses_latest.course_name FROM student_latest LEFT JOIN courses_latest ON student_latest.selected_course = courses_latest.course_id;


-- right outer join
-- ===================
-- all the matching records from left and right table are considered
-- +
-- all the non matching records in the right table which does not have the match in the right padded with null

SELECT student_latest.student_fname, student_latest.student_lname, courses_latest.course_name FROM student_latest RIGHT JOIN courses_latest ON student_latest.selected_course = courses_latest.course_id;

SELECT * FROM COURSES_LATEST;

DELETE FROM student_latest WHERE selected_course=3;
SELECT * FROM student_latest;


-- full outer join
-- ====================
-- all the matching records
-- +
-- non matching records from left
-- +
-- non matching records form right

SELECT student_latest.student_fname, student_latest.student_lname, courses_latest.course_name FROM student_latest LEFT JOIN courses_latest ON student_latest.selected_course = courses_latest.course_id
UNION
SELECT student_latest.student_fname, student_latest.student_lname, courses_latest.course_name FROM student_latest RIGHT JOIN courses_latest ON student_latest.selected_course = courses_latest.course_id;



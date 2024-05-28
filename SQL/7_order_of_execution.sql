
SELECT DISTINCT source_of_joining FROM student ORDER BY enrollment_Date DESC;  -- this will be an error

SELECT source_of_joining FROM student;

-- order of execution
-- ==============
-- FROM (LOADING THE TABLE)
-- SELECT (PROJECTING source_of_joining)

SELECT source_of_joining, enrollment_Date FROM student;
-- order of execution
-- ==================
-- FROM (LOADING THE TABLE)
-- SELECT (PROJECTING source_of_joining, enrollement_date)


SELECT source_of_joining, enrollment_Date FROM student ORDER BY enrollment_date;
-- order of execution
-- ==================
-- FROM (LOADING THE TABLE)

-- SELECT (PROJECTING source_of_joining, enrollement_date)

-- order by (based on enrollment date it will order by)




SELECT source_of_joining FROM student ORDER BY enrollment_date;
-- order of execution  -- ORDER OF EXECUTION WILL BE SAME
-- ==================
-- FROM (LOADING THE TABLE)

-- SELECT (PROJECTING source_of_joining, enrollement_date)

-- order by (based on enrollment date it will order by)



SELECT DISTINCT source_of_joining FROM student ORDER BY enrollment_date;
-- order of execution
-- ===================

-- FROM (LOADING THE TABLE)

-- SELECT (PROJECTION source_of_joining, enrollment_date)alter

-- DISTINCT
-- here is DISTINCT is working on both (source_of_joining and enrollment_date) which give logical wrong and give wrong output
-- but we want it to work only with source_of_joining, so it is giving an error

-- order by (based on enrollment_date it will order by)
-- select source_of_joining from students order by enrollment_date



-- WHERE vs HAVING clause
-- =======================

SELECT source_of_joining, count(*) as total FROM student GROUP BY source_of_joining;

-- i want to know the leas source through with more than 6 person has registered 
SELECT source_of_joining, count(*) AS total FROM student GROUP BY source_of_joining WHERE total > 6; -- this will show error
-- where clause is used to filter the individual records before aggregation

SELECT source_of_joining, count(*) AS total FROM student GROUP BY source_of_joining HAVING total > 6;
-- having clause is used to filter the individual records after aggregation

-- i want to know the count of people who registered through linkedin
SELECT source_of_joining, count(*) AS total FROM student GROUP BY source_of_joining HAVING source_of_joining='Referral' ;
SELECT source_of_joining, count(*) AS total FROM student WHERE source_of_joining='Referral' GROUP BY source_of_joining;


-- to use where and having in same query
-- =====================================
-- the location from which more than 1 student has joined & the students experience is more than 5 years
SELECT location, count(*) AS total FROM student WHERE years_of_exp > 5 GROUP BY location HAVING total > 1;



-- where is used before group by and do filtering on individual revords

-- having is used after group by and do filtering on aggregated records

-- we can also use having and where in same query

-- where is more performant than having













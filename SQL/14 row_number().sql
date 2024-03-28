
SELECT firstname, lastname, salary, row_number() OVER (ORDER BY salary DESC) AS sno FROM employee;


-- find 5th highest salary
SELECT * FROM (SELECT firstname, lastname, salary, row_number() OVER (ORDER BY salary DESC) AS sno FROM employee) TEMPTABLE WHERE sno=5;


-- to assign row number for partitions based on each location...
SELECT firstname, lastname, location, salary, row_number() OVER (partition by location ORDER BY salary DESC) from employee;


-- to find the highest salary getters at each location
SELECT * FROM (SELECT firstname, lastname, location, salary, row_number() OVER (PARTITION BY location ORDER BY salary DESC) AS rownum FROM employee) TEMPTABLE WHERE rownum = 1;




-- when we use row_number()
-- must use the order by clause
-- we can also use the parttition by - optional 
-- the rownumber starts from 1 for every partition

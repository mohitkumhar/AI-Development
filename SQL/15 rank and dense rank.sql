select * FROM employee;

-- this will list different numbers to all duplicate
SELECT firstname, lastname, salary ,ROW_NUMBER() OVER (ORDER BY salary) FROM employee;

-- this will treat duplicate as duplicate and not list them different
SELECT firstname, lastname, salary, RANK() OVER (ORDER BY salary) FROM employee;

SELECT firstname, lastname, salary, DENSE_RANK() OVER (ORDER BY salary) FROM employee;

-- if there are no dduplicates then row number, rnak and dense rank lead to similar results..

-- only the difference comes when there are duplicates..

-- rank - for duplicates same rank is assigned and the for the next entry it skips the ranks...

-- dense rank - it does not skip any ranks in between 

-- whenever we dont have duplicates use row_number



-- ## There is some competition ##
-- i want to find the top 3 positions...

-- NUMBER 		RANK		DENSE RANK
-- 100 	-	1		-	1
-- 100 	-	1		-	1
-- 98 		-	3		-	2
-- 97 		-	4		-	3
-- 97 		-	4		-	3
-- 96 		-	6		-	4




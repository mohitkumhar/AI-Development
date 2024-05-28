-- SELECT
-- ============

-- for select all columns
SELECT * FROM employee;

-- for selecting specific column
SELECT firstname, lastname FROM employee;

-- for selecting specific rows
-- select by applying a where clause (filter condition)
SELECT * FROM employee WHERE age  < 22;

SELECT * FROM employee WHERE firstname='MOHIT';  -- be default it is case insensetive

SELECT * FROM employee WHERE BINARY firstname='mohit'; -- this is case sensitive

-- alias for column name
SELECT firstname AS name, lastname AS surname FROM employee;


-- UPDATE
-- ============

UPDATE employee SET lastname='prajapat' WHERE firstname='mohit';

UPDATE employee SET lastname='kumhar'; -- this will update whole table

-- to check multiple conditions for updating if single condition is more than one
UPDATE employee SET lastname='prajapat' WHERE firstname='mohit' and age=19;


-- DELETE
-- =========
DELETE FROM employee WHERE id=3; -- delete according to condition

DELETE FROM employee; -- will delete whole table elements



-- alter command
-- ===============
-- alter is used to update the structure of table
ALTER TABLE employee ADD COLUMN jobtitle VARCHAR(50); -- to add extra column

ALTER TABLE employee DROP COLUMN jobtitle; -- to drop the column

ALTER TABLE employee MODIFY COLUMN firstname VARCHAR(50); -- this will change the input limit of variable

ALTER TABLE employee DROP PRIMARY KEY; -- will remove primary key from key

ALTER TABLE employee ADD PRIMARY KEY(id); -- will add primary key to that given column


-- DDL vs DML
-- =============
-- Data Definition Language - deals with table structure

-- Create, Alter, Drop - DDL Commands

-- Data Manipulation Language - here we deal the data directly

-- insert, update, delete - DML command

-- Truncate 
-- ===========
TRUNCATE TABLE employee;
-- truncate internally drops the table and recreates it
-- delete deletes the data one-by-one








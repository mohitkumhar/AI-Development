-- Topics
-- Session -3
-- =================

-- CRUD Operation 
-- Insert Operation 
-- Insert Statement
-- Simple Statement
-- Multiple Inserts
-- Datatype Mismatch
-- Null vs Not Null
-- Default Values
-- =x=x=x=x=x=x=x=x=x=x=x=x=



-- Learn SQL the Right Way
-- =========================

-- CRUD Operations

-- create - insert statements
-- read - select statements
-- update - update statements
-- delete - delete statements

-- Creation of table and Insert Statements


-- ######## 

-- employee table

-- you prefer to hire from bangalore
CREATE TABLE employee
(
    firstname VARCHAR(20),
    middlename VARCHAR(20),
    lastname VARCHAR(20),
    age INT,
    salary FLOAT,
    location VARCHAR(20)
);


SHOW TABLES;  -- will show the tables available in the database


-- to insert data in table-
INSERT INTO employee(firstname, middlename, lastname, age, salary, location) VALUES ('mohit', 'kumhar', 'prajapat', 19, 10000000, 'bangalore');  -- this is recommanded method

-- OR

INSERT INTO employee VALUES ('mohit', 'kumhar', 'prajapat', 19, 10000000, 'bangalore');


-- if we dont want to insert any specific data (in this case middlename is not inserted)
INSERT INTO employee(firstname, lastname, age, salary, location) VALUES ('Landsenberg', 'Shelby', 19, 10000000, 'bangalore');


-- # if we want to use inverted comma in values which wrting the insert command
-- # we can use 
-- "mohit's"  # this will pass the value in table as mohit's
-- # or we can also write 
-- 'mohit\'s' 


-- to insert multiple rows in table
INSERT INTO employee(firstname, middlename, lastname, age, salary, location) VALUES ('mohit', 'kumhar', 'prajapat', 19, 100000, 'udaipur'), ('heisenberg', 'grambell', 'grambell', 41, 1000000, 'WilstonDuke');


-- to restrict user input NULL value in table
CREATE TABLE employee
(
    firstname VARCHAR(20) NOT NULL, 
    middlename VARCHAR(20),
    lastname VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    salary FLOAT NOT NULL,
    location VARCHAR(20) NOT NULL
);


-- default values
-- ==============
CREATE TABLE employee
(
    firstname VARCHAR(20) NOT NULL, 
    middlename VARCHAR(20),
    lastname VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    salary FLOAT NOT NULL,
    location VARCHAR(20) DEFAULT 'bangalore'  -- this will use value banglore if user not input anything
);


-- conbination of NOT NULL and DEFAULT
-- ====================================
CREATE TABLE employee
(
    firstname VARCHAR(20) NOT NULL, 
    middlename VARCHAR(20),
    lastname VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    salary FLOAT NOT NULL,
    location VARCHAR(20) NOT NULL DEFAULT 'bangalore'  -- this will use value banglore if user not input anything
);












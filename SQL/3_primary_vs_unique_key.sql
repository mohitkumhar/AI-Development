-- Primary Key 
-- Auto Increment Keys
-- Unique Key
-- Primary Key vs Unique Key


-- create table using primary key so that it cannot be use by other to avoid confusion of same data
CREATE TABLE employee
(
	id INT PRIMARY KEY,
    firstname VARCHAR(20),
    middlename VARCHAR(20),
    lastname VARCHAR(20),
    age INT,
    salary FLOAT,
    location VARCHAR(20)
);

INSERT INTO employee(id, firstname, middlename, lastname, age, salary, location) 
VALUES (1, 'mohit', 'kumhar', 'prajapat', 19, 100000, 'udaipur'), 
(2,'heisenberg', 'grambell', 'grambell', 41, 1000000, 'WilstonDuke');


-- to give primary key in combination
-- use- PRIMARY KEY(variable_name1, variable_name2, ...)
CREATE TABLE employee
(
	id INT,
    firstname VARCHAR(20),
    middlename VARCHAR(20),
    lastname VARCHAR(20),
    age INT,
    salary FLOAT,
    location VARCHAR(20),
    PRIMARY KEY(id)    
);


-- # AUTO_INCREMENT
CREATE TABLE employee
(
	id INT AUTO_INCREMENT,
    firstname VARCHAR(20),
    middlename VARCHAR(20),
    lastname VARCHAR(20),
    age INT,
    salary FLOAT,
    location VARCHAR(20),
    PRIMARY KEY(id)    
);


INSERT INTO employee(firstname, middlename, lastname, age, salary, location) 
VALUES ('mohit', 'kumhar', 'prajapat', 19, 100000, 'udaipur'), 
('heisenberg', 'grambell', 'grambell', 41, 1000000, 'WilstonDuke');



-- # UNIQUE KEY
-- we can only one primary key, and primary key cannot hold any NULL values
-- we should use primary key wehn we have to uniquely identify any record

-- unique key can hold NULL

-- for example in MySQL a UNIQUE KEY can hold any number of NULL values 
-- in some if the other famous DB's unique key hold only one NULL value

-- so the purpose of unique key is to make sure the values do not duplicate
-- unique key can be more than one but primary key can be only one

CREATE TABLE employee
(
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY(firstname, lastname) -- this will concate the firstname and lastname and then check if it already exist or not 
);

CREATE TABLE employee
(
	id VARCHAR(20) UNIQUE KEY,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    age INT NOT NULL
);






CREATE TABLE employee
(
	firstname VARCHAR(20),
	lastname VARCHAR(20),
    age INT,
    salary INT,
    location VARCHAR(20)
);

INSERT INTO employee(firstname, lastname, age, salary, location) VALUES
('sachin', 'sharma', '28', 1000, 'bangalore'),
('shane', 'warne', 30, 20000, 'bangalore'),
('rohit', 'sharma', 32, 30000, 'hyderabad'),
('shikhar', 'dhawan', 32, 25000, 'hyderabad'),
('rahul', 'dravid', 31, 20000, 'bangalore'),
('saurabh', 'ganguly', 32, 15000, 'pune'),
('kapil', 'dev', 34, 10000, 'pune');

-- how many people are form each location and avg salary at each location

SELECT location, count(location), AVG(salary) FROM employee GROUP BY location;


SELECT firstname, lastname, location, count(location), AVG(salary) FROM employee GROUP BY location; -- this will lead to an error

SELECT firstname, lastname, employee.location, total_count, avg_salary FROM employee JOIN 
(SELECT location, count(location) AS total_count, AVG(salary) AS avg_salary FROM employee GROUP BY location) TEMPTABLE ON employee.location = TEMPTABLE.location;


-- we can use OVER PARTITION BY to achieve this easily
SELECT firstname, lastname, location, count(location) OVER (PARTITION BY location) AS count_total, AVG(SALARY) OVER (PARTITION BY location) AS avg_salary FROM employee;



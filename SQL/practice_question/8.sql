-- 8. GROUP BY Clause
-- 
-- Write a SQL query to count the number of orders for each customer from the `orders` table and group the results by `customer_id`.

USE practice;

SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id;


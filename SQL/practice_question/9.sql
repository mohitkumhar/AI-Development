-- 9. HAVING Clause
--    
-- Write a SQL query to count the number of orders for each customer from the `orders` table,
-- group the results by `customer_id`, and filter the groups to only include those with more than 5 orders.

USE practice;

SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY customer_id HAVING order_count > 5;


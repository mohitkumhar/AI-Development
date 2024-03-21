-- 6. JOIN Operation
-- 
-- Write a SQL query to join the `orders` table with the `customers` table on the 
-- `customer_id` and select the `order_id` and `customer_name`.

USE practice;

SELECT orders.order_id, customers.customer_name FROM orders JOIN customers ON orders.order_id = customers.customer_id;

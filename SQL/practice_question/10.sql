-- 10. Subqueries
--     
-- Write a SQL query to find all products from the `products` table that have a `price` greater than the average price.

USE practice;

SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);



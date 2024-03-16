-- 11. **Window Functions**
--
-- Write a SQL query to calculate a running total of `sales` in the `sales` table, partitioned by `region` and ordered by `sale_date`.

USE practice;

SELECT sale_id, product_id, amount, sale_date, region, count(region) OVER (PARTITION BY region ORDER BY sale_date) AS total_from_region FROM sales;


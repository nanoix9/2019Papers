-- Q1 Determine the top 5 products in Dec 2019 in terms of total sales
-- PRODUCT_NAME TOTAL_SALES RANK 

WITH s AS (
    SELECT product_id, sum(amount) AS total_sales 
    FROM Sales s
    JOIN DateDim d
    ON s.date_id = d.date_id
    WHERE d.year = 2019 AND d.month = 12
    GROUP BY product_id
),
sr AS (
    SELECT product_name, 
           total_sales, 
           RANK() OVER(ORDER BY total_sales DESC) rank
    FROM s
    JOIN Product p
    ON s.product_id = p.product_id
)
SELECT product_name, total_sales, rank
FROM sr
WHERE rank <= 5;

-- Q2 Determine which store produced highest sales in the whole year?
-- STORE_NAME TOTAL_SALES RANK 

WITH s AS (
    SELECT store_id, sum(amount) AS total_sales 
    FROM Sales s
    JOIN DateDim d
    ON s.date_id = d.date_id
    WHERE d.year = 2019
    GROUP BY store_id
),
sr AS (
    SELECT store_name, 
           total_sales
    FROM s
    JOIN Store t
    ON s.store_id = t.store_id
    ORDER BY total_sales DESC
)
SELECT store_name, total_sales, ROWNUM AS rank
FROM sr
WHERE ROWNUM = 1;

-- Q3 Determine the top 3 products for a month (say, Dec 2019), and 
-- for the 2 months before that, in terms of total sales.
-- PRODUCT_NAME SUM(TOTAL_SALES) RANK 

-- Q4 Create a materialised view called “STOREANALYSIS” that presents 
-- the product-wise sales analysis for each store. The results should be ordered 
-- by StoreID and then ProductID.
-- STOREID PRODUCTID SUM(STORE_TOTAL) 

CREATE MATERIALIZED VIEW StoreAnalysis
ENABLE QUERY REWRITE
AS
SELECT store_id, product_id, SUM(amount)
FROM Sales
ORDER BY store_id, product_id;

-- Q5 Think about what information can be retrieved from the materialised view
-- created in Q4 using ROLLUP or CUBE concepts and provide some useful information
-- of your choice for management.

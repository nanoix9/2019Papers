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
/

-- Q3 Determine the top 3 products for a month (say, Dec 2019), and 
-- for the 2 months before that, in terms of total sales.
-- PRODUCT_NAME SUM(TOTAL_SALES) RANK 

DROP TYPE T_TABLE_COLL;
DROP TYPE T_TABLE;
/
CREATE OR REPLACE TYPE T_TABLE IS OBJECT
(
    product_name VARCHAR2(30),
    total_sales NUMBER,
    rank NUMBER,
    month NUMBER,
    year NUMBER
);
/
CREATE OR REPLACE TYPE T_TABLE_COLL IS TABLE OF T_TABLE;
/
CREATE OR REPLACE
FUNCTION top_in_months(
    top_k IN NUMBER,
    start_month IN NUMBER, 
    start_year IN NUMBER,
    num_months IN NUMBER)
RETURN T_TABLE_COLL PIPELINED
IS
    CURSOR top_products (month_in IN NUMBER, year_in IN NUMBER)
    IS 
        SELECT product_name, total_sales, ROWNUM AS rank, month, year
        FROM (
            SELECT product_name, total_sales, ROWNUM AS rank, month, year
            FROM (SELECT product_name, SUM(amount) AS total_sales, month, year
                FROM Sales s, DateDim d, Product p
                WHERE s.date_id = d.date_id 
                    AND s.product_id = p.product_id
                    AND month = month_in
                    AND year = year_in
                GROUP BY product_name, month, year)
            ORDER BY total_sales DESC
        )
        WHERE ROWNUM <= top_k;
    
    query_month NUMBER := 0;
    query_year NUMBER := 0;
BEGIN
    query_month := start_month;
    query_year := start_year;

    FOR k in 1..top_k
    LOOP
        FOR i IN top_products(query_month, query_year)
        LOOP
            PIPE ROW (T_TABLE(i.product_name, i.total_sales, i.rank, i.month, i.year));
        END LOOP;

        IF query_month = 1 THEN
            query_month := 12;
            query_year := query_year - 1;
        ELSE
            query_month := query_month - 1;
        END IF;
    END LOOP;
END;
/
SELECT * FROM TABLE(top_in_months(3, 12, 2019, 3));
/

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

CREATE OR REPLACE
FUNCTION foo()
RETURN T_TABLE_COLL
IS
    top_products T_TABLE_COLL;
begin
    SELECT T_TABLE (product_id, amount)
    INTO top_products
    FROM Sales 
    WHERE date_id = '20190505';
    return(top_products);
end;

-- Q5 Think about what information can be retrieved from the materialised view
-- created in Q4 using ROLLUP or CUBE concepts and provide some useful information
-- of your choice for management.



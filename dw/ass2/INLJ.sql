
-- drop table TEST2;

-- CREATE TABLE "TEST2" (tid NUMBER(8), "txt1" VARCHAR2(100));

-- SELECT "txt1" FROM TEST2;
-- SELECT count(*) FROM TEST2;

DECLARE
    bulk_size PLS_INTEGER := 50;
    
    CURSOR ds_cursor 
    IS 
        SELECT TRANSACTIONS_ID,
               PRODUCT_ID,
               CUSTOMER_ID,
               CUSTOMER_NAME,
               STORE_ID,
               STORE_NAME,
               T_DATE,
               QUANTITY
       FROM TRANSACTIONS;
    
    -- TYPE trans_t IS TABLE OF TRANSACTIONS%ROWTYPE;
    -- trans_bulk trans_t;

    -- field types and variables from transaction table
    TYPE trans_id_t IS TABLE OF TRANSACTIONS.TRANSACTIONS_ID%TYPE;
    trans_id_var trans_id_t;
    TYPE product_id_t IS TABLE OF TRANSACTIONS.PRODUCT_ID%TYPE;
    product_id_var product_id_t;
    TYPE customer_id_t IS TABLE OF TRANSACTIONS.CUSTOMER_ID%TYPE;
    customer_id_var customer_id_t;
    TYPE customer_name_t IS TABLE OF TRANSACTIONS.CUSTOMER_NAME%TYPE;
    customer_name_var customer_name_t;
    TYPE store_id_t IS TABLE OF TRANSACTIONS.STORE_ID%TYPE;
    store_id_var store_id_t;
    TYPE store_name_t IS TABLE OF TRANSACTIONS.STORE_NAME%TYPE;
    store_name_var store_name_t;
    TYPE t_date_t IS TABLE OF TRANSACTIONS.T_DATE%TYPE;
    t_date_var t_date_t;
    TYPE quantity_t IS TABLE OF TRANSACTIONS.QUANTITY%TYPE;
    quantity_var quantity_t;

    date_id_var CHAR(8);

    -- field types and variables from master table
    -- TYPE product_name_t IS TABLE OF MASTERDATA.PRODUCT_NAME%TYPE;
    -- product_name_var product_name_t;
    -- TYPE supplier_t IS TABLE OF MASTERDATA.SUPPLIER_ID%TYPE;
    -- supplier_var supplier_t;
    -- TYPE supplier_name_t IS TABLE OF MASTERDATA.SUPPLIER_NAME%TYPE;
    -- supplier_name_var supplier_name_t;
    -- TYPE price_t IS TABLE OF MASTERDATA.PRICE%TYPE;
    -- price_var price_t;
    md_var MASTERDATA%ROWTYPE;
BEGIN
    OPEN ds_cursor;
    -- FOR i IN 1 .. 3       -- uncomment this line for testing with small amount of data
    LOOP
        -- FETCH ds_cursor BULK COLLECT INTO trans_bulk LIMIT bulk_size;
        -- FETCH ds_cursor BULK COLLECT INTO trans_bulk LIMIT bulk_size;
        -- EXIT WHEN trans_bulk.COUNT = 0;
        FETCH ds_cursor 
        BULK COLLECT INTO 
            trans_id_var, 
            product_id_var, 
            customer_id_var,
            customer_name_var,
            store_id_var,
            store_name_var,
            t_date_var,
            quantity_var
        LIMIT bulk_size;

        EXIT WHEN trans_id_var.COUNT = 0;

        -- -- DBMS_OUTPUT.PUT_LINE('id: ' ||trans.TRANSACTIONS_ID);
        -- -- FORALL i IN trans_bulk.FIRST .. trans_bulk.LAST
        -- -- FORALL i IN trans_id_var.FIRST .. trans_id_var.LAST
        -- FOR i IN trans_id_var.FIRST .. trans_id_var.LAST
        -- LOOP
        --     INSERT INTO TEST2 (tid, "txt1") 
        --     SELECT trans_id_var(i), PRODUCT_NAME
        --     FROM MASTERDATA m
        --     WHERE m.PRODUCT_ID = product_id_var(i);
        -- END LOOP;
             -- trans_id_var(i));
        -- FOR i IN trans_bulk.FIRST .. trans_bulk.LAST
        -- LOOP
        --     INSERT INTO TEST2 ("txt1") VALUES (trans_bulk(i).CUSTOMER_NAME);
        -- END LOOP;


        FOR i IN trans_id_var.FIRST .. trans_id_var.LAST
        LOOP
            SELECT * INTO md_var 
            FROM MASTERDATA 
            WHERE PRODUCT_ID = product_id_var(i);

            INSERT INTO Product (product_id, product_name)
            SELECT md_var.PRODUCT_ID, md_var.PRODUCT_NAME
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Product
                    WHERE PRODUCT_ID = product_id_var(i) 
                        AND PRODUCT_NAME = md_var.PRODUCT_NAME
                );

            INSERT INTO Supplier (supplier_id, supplier_name)
            SELECT md_var.SUPPLIER_ID, md_var.SUPPLIER_NAME
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Supplier p
                    WHERE SUPPLIER_ID = md_var.SUPPLIER_ID 
                        AND SUPPLIER_NAME = md_var.SUPPLIER_NAME
                );

            INSERT INTO Store (store_id, store_name)
            SELECT store_id_var(i), store_name_var(i)
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Store 
                    WHERE STORE_ID = store_id_var(i) 
                        AND STORE_NAME = store_name_var(i)
                );

            INSERT INTO Customer (customer_id, customer_name)
            SELECT customer_id_var(i), customer_name_var(i)
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM customer 
                    WHERE CUSTOMER_ID = customer_id_var(i) 
                        AND CUSTOMER_NAME = customer_name_var(i)
                );

            date_id_var := TO_CHAR(t_date_var(i), 'YYYYMMDD');
            INSERT INTO DateDim (date_id, day, day_of_week, week, month, quarter, year)
            SELECT date_id_var,
                   EXTRACT(DAY FROM t_date_var(i)),
                   TO_CHAR(t_date_var(i), 'D'),
                   TO_CHAR(t_date_var(i), 'WW'),
                   EXTRACT(MONTH FROM t_date_var(i)),
                   TO_CHAR(t_date_var(i), 'Q'),
                   EXTRACT(YEAR FROM t_date_var(i))
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM DateDim 
                    WHERE DATE_ID = date_id_var 
                );

            INSERT INTO Sales (sales_id, 
                               product_id,
                               supplier_id,
                               customer_id, 
                               store_id, 
                               date_id, 
                               quantity, 
                               amount)
            VALUES (trans_id_var(i),
                    product_id_var(i),
                    md_var.SUPPLIER_ID,
                    customer_id_var(i),
                    store_id_var(i),
                    date_id_var,
                    quantity_var(i),
                    quantity_var(i) * md_var.PRICE);
        END LOOP;
        

    END LOOP;

    CLOSE ds_cursor;
END;

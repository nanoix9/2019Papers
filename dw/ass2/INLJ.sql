--------------------------------------------------------------------------------
--                      Index Nested Loop Join
--------------------------------------------------------------------------------

DECLARE
    -- the number of rows to fetch by a cursor at each time
    bulk_size PLS_INTEGER := 50;
    
    -- the cursor is simply a selection of all columns of TRANSACTIONS table.
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

    -- date ID is a surrogate key like "YYYYMMDD"
    date_id_var CHAR(8);

    -- variable for a row in MASTERDATA table
    md_var MASTERDATA%ROWTYPE;

BEGIN
    OPEN ds_cursor;
    -- FOR i IN 1 .. 3       -- uncomment this line for testing with small amount of data
    LOOP
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

        -- loop on the bulk just fetched and join with master data row-by-row
        FOR i IN trans_id_var.FIRST .. trans_id_var.LAST
        LOOP
            -- read the corresponding row from MD by the same "product_id"
            SELECT * INTO md_var 
            FROM MASTERDATA 
            WHERE PRODUCT_ID = product_id_var(i);

            -- fill Product dimension table. Insert only if it doesn't exist.
            --     Compared both product_name along with product_id because
            --     it's assumed that there won't be multiple product names
            --     for one product ID. If such thing happened there will raise
            --     an error, requiring manual inspection and correction.
            --     Same logic applies to other tables.
            -- trick: "dual" is a dummy table with only one row 
            --        in order to form valid `SELECT` statement
            INSERT INTO Product (product_id, product_name)
            SELECT md_var.PRODUCT_ID, md_var.PRODUCT_NAME
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Product
                    WHERE PRODUCT_ID = product_id_var(i) 
                        AND PRODUCT_NAME = md_var.PRODUCT_NAME
                );

            -- fill Supplier dimension table. 
            INSERT INTO Supplier (supplier_id, supplier_name)
            SELECT md_var.SUPPLIER_ID, md_var.SUPPLIER_NAME
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Supplier p
                    WHERE SUPPLIER_ID = md_var.SUPPLIER_ID 
                        AND SUPPLIER_NAME = md_var.SUPPLIER_NAME
                );

            -- fill Customer dimension table. 
            INSERT INTO Customer (customer_id, customer_name)
            SELECT customer_id_var(i), customer_name_var(i)
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM customer 
                    WHERE CUSTOMER_ID = customer_id_var(i) 
                        AND CUSTOMER_NAME = customer_name_var(i)
                );

            -- fill Store dimension table. 
            INSERT INTO Store (store_id, store_name)
            SELECT store_id_var(i), store_name_var(i)
            FROM dual
            WHERE NOT EXISTS (
                    SELECT * 
                    FROM Store 
                    WHERE STORE_ID = store_id_var(i) 
                        AND STORE_NAME = store_name_var(i)
                );

            -- fill Date dimension table. 
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

            -- fill Sales fact table. 
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

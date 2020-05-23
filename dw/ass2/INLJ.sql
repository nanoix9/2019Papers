
drop table TEST2;

CREATE TABLE "TEST2" ("txt1" VARCHAR2(100));

SELECT "txt1" FROM TEST2;

DECLARE
    bulk_size PLS_INTEGER := 2;
    
    CURSOR ds_cursor 
    IS SELECT TRANSACTIONS_ID, PRODUCT_ID FROM TRANSACTIONS;
    
    -- TYPE trans_t IS TABLE OF TRANSACTIONS%ROWTYPE;
    -- trans_bulk trans_t;

    TYPE trans_id_t IS TABLE OF TRANSACTIONS.TRANSACTIONS_ID%TYPE;
    trans_id trans_id_t;
    TYPE product_id_t IS TABLE OF TRANSACTIONS.PRODUCT_ID%TYPE;
    product_id product_id_t;
    TYPE customer_id_t IS TABLE OF TRANSACTIONS.CUSTOMER_ID%TYPE;
    customer_id customer_id_t;
    TYPE customer_name_t IS TABLE OF TRANSACTIONS.CUSTOMER_NAME%TYPE;
    customer_name customer_name_t;
    TYPE store_id_t IS TABLE OF TRANSACTIONS.STORE_ID%TYPE;
    store_id store_id_t;
    TYPE store_name_t IS TABLE OF TRANSACTIONS.STORE_NAME%TYPE;
    store_name store_name_t;
    TYPE t_date_t IS TABLE OF TRANSACTIONS.T_DATE%TYPE;
    t_date t_date_t;
    TYPE quantity_t IS TABLE OF TRANSACTIONS.QUANTITY%TYPE;
    quantity quantity_t;
BEGIN
    OPEN ds_cursor;
    FOR i IN 1 .. 3
    LOOP
        -- FETCH ds_cursor BULK COLLECT INTO trans_bulk LIMIT bulk_size;
        -- FETCH ds_cursor BULK COLLECT INTO trans_bulk LIMIT bulk_size;
        -- EXIT WHEN trans_bulk.COUNT = 0;
        FETCH ds_cursor 
        BULK COLLECT INTO trans_id, product_id 
        LIMIT bulk_size;

        EXIT WHEN trans_id.COUNT = 0;

        -- DBMS_OUTPUT.PUT_LINE('id: ' ||trans.TRANSACTIONS_ID);
        -- FORALL i IN trans_bulk.FIRST .. trans_bulk.LAST
        -- FORALL i IN trans_id.FIRST .. trans_id.LAST
        FOR i IN trans_id.FIRST .. trans_id.LAST
        LOOP
            INSERT INTO TEST2 ("txt1") 
            SELECT PRODUCT_NAME 
            FROM MASTERDATA m
            WHERE m.PRODUCT_ID = product_id(i);
        END LOOP;
             -- trans_id(i));
        -- FOR i IN trans_bulk.FIRST .. trans_bulk.LAST
        -- LOOP
        --     INSERT INTO TEST2 ("txt1") VALUES (trans_bulk(i).CUSTOMER_NAME);
        -- END LOOP;

    END LOOP;
    CLOSE ds_cursor;
END;

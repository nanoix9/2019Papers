--------------------------------------------------------------------------------
--         COMP810 Data Warehousing and Big Data Assessment 2
-- Author: Stone Fang 
-- Student ID: 19049045
-- email: nanoix9@gmail.com
--
-- This script creates star-schema for NatureFresh DW
-- The script should create all dimension and fact tables table in DW 
-- 
-- if any table with same name already exists, the table should be droped. 
-- It also applies all primary and foreign keys on the right attributes.
--------------------------------------------------------------------------------


-- drop sales table first as there are foreign key dependencies on dimension table
DROP TABLE Sales;

DROP TABLE Product;
DROP TABLE Supplier;
DROP TABLE Customer;
DROP TABLE Store;
DROP TABLE DateDim;

--------------------------------------------------------------------------------
-- DDL for Dimension Tables
--------------------------------------------------------------------------------

CREATE TABLE Product (
    product_id      VARCHAR2(6)  NOT NULL,
    product_name    VARCHAR2(30) NOT NULL, 
    CONSTRAINT product_pk PRIMARY KEY (product_id));


CREATE TABLE Supplier (
    supplier_id    VARCHAR2(5)   NOT NULL, 
    supplier_name  VARCHAR2(30)  NOT NULL, 
    CONSTRAINT supplier_pk PRIMARY KEY (supplier_id));


CREATE TABLE Customer (
    customer_id      VARCHAR2(4)    NOT NULL, 
    customer_name    VARCHAR2(30)   NOT NULL, 
    CONSTRAINT customer_pk PRIMARY KEY (customer_id));


CREATE TABLE Store (
    store_id         VARCHAR2(4)   NOT NULL, 
    store_name       VARCHAR2(20)  NOT NULL,
    CONSTRAINT store_pk PRIMARY KEY (store_id));


CREATE TABLE DateDim (
    date_id      VARCHAR2(8)     NOT NULL,
    day          NUMBER(2)       NOT NULL,
    day_of_week  NUMBER(1)       NOT NULL,
    week         NUMBER(2)       NOT NULL,
    month        NUMBER(2)       NOT NULL,
    quarter      NUMBER(1)       NOT NULL,
    year         NUMBER(4)       NOT NULL,
    CONSTRAINT date_pk PRIMARY KEY (date_id),
    CONSTRAINT day_range         CHECK (day          BETWEEN 1 AND 31),
    CONSTRAINT day_of_week_range CHECK (day_of_week  BETWEEN 1 AND 7),
    CONSTRAINT week_range        CHECK (week         BETWEEN 1 AND 53),
    CONSTRAINT month_range       CHECK (month        BETWEEN 1 AND 12),
    CONSTRAINT quater_range      CHECK (quarter      BETWEEN 1 AND 4)
    );

-- Create indexes on all level
-- Indexes on primary key will be created automatically
CREATE INDEX Product_product_name_i   ON Product  (product_name);
CREATE INDEX Supplier_supplier_name_i ON Supplier (supplier_name);
CREATE INDEX Customer_customer_name_i ON Customer (customer_name);
CREATE INDEX Store_store_name_i       ON Store    (store_name);
CREATE INDEX Date_multi_ymd_i         ON DateDim  (year, month, day);
CREATE INDEX Date_multi_ywd_i         ON DateDim  (year, week, day_of_week);
CREATE INDEX Date_multi_yq_i          ON DateDim  (year, quarter);

--------------------------------------------------------
--  DDL for Fact Table: Sales
--------------------------------------------------------

CREATE TABLE Sales (
    sales_id      NUMBER(8)     NOT NULL, 
    product_id    VARCHAR2(6)   NOT NULL, 
    supplier_id   VARCHAR2(6)   NOT NULL, 
    customer_id   VARCHAR2(4)   NOT NULL,
    store_id      VARCHAR2(4)   NOT NULL, 
    date_id       VARCHAR2(8)   NOT NULL,
    quantity      NUMBER(3,0)   NOT NULL,
    amount        NUMBER(8,2)   NOT NULL,
    CONSTRAINT SALES_PK    PRIMARY KEY (sales_id), 
    CONSTRAINT product_fk  FOREIGN KEY (product_id)  REFERENCES Product  (product_id),
    CONSTRAINT supplier_fk FOREIGN KEY (supplier_id) REFERENCES Supplier (supplier_id),
    CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    CONSTRAINT store_fk    FOREIGN KEY (store_id)    REFERENCES Store    (store_id),
    CONSTRAINT date_fk     FOREIGN KEY (date_id)     REFERENCES DateDim  (date_id)
    );

-- create indexes on all foriegn keys for query optimisation
CREATE INDEX Sales_product_fk_i   ON Sales (product_id);
CREATE INDEX Sales_supplier_fk_i  ON Sales (supplier_id);
CREATE INDEX Sales_customer_fk_i  ON Sales (customer_id);
CREATE INDEX Sales_store_fk_i     ON Sales (store_id);
CREATE INDEX Sales_date_fk_i      ON Sales (date_id);

--------------------------------------------------------------------------------
-- The following is just showing informations of tables just created.
-- Not mandatory for code execution.
--------------------------------------------------------------------------------
-- describe tables
DESC Product;
DESC Store;
DESC Supplier;
DESC Customer;
DESC DateDim;
DESC Sales;

-- Show constraints of all tables. 
-- The table names are all in uppercase in the `user_constraints` table.
SELECT * FROM user_constraints WHERE table_name = 'SALES';
SELECT * FROM user_constraints WHERE table_name = 'PRODUCT';
SELECT * FROM user_constraints WHERE table_name = 'STORE';
SELECT * FROM user_constraints WHERE table_name = 'SUPPLIER';
SELECT * FROM user_constraints WHERE table_name = 'CUSTOMER';
SELECT * FROM user_constraints WHERE table_name = 'SALES';

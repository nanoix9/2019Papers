# Exploratory data analysis

```

select CUSTOMER_ID, WM_CONCAT(DISTINCT CUSTOMER_NAME) FROM TRANSACTIONS group by CUSTOMER_ID;
select CUSTOMER_ID, COUNT(DISTINCT CUSTOMER_NAME) FROM TRANSACTIONS group by CUSTOMER_ID;

select STORE_ID, COUNT(DISTINCT STORE_NAME) FROM TRANSACTIONS group by STORE_ID;

select SUPPLIER_ID, COUNT(DISTINCT SUPPLIER_NAME) FROM TRANSACTIONS group by SUPPLIER_ID;

select * from (
    select PRODUCT_ID, STORE_ID, T_DATE, COUNT(CUSTOMER_ID) as nc, COUNT(DISTINCT CUSTOMER_ID) as ndc FROM TRANSACTIONS group by PRODUCT_ID, STORE_ID, T_DATE) t
where nc > ndc;

select PRODUCT_ID, STORE_ID, T_DATE, COUNT(CUSTOMER_ID) - COUNT(DISTINCT CUSTOMER_ID) FROM TRANSACTIONS group by PRODUCT_ID, STORE_ID, T_DATE;

select * from transactions where product_id='P-1001' and store_id='S-3' and t_date='16/11/19'

```


# Assessment

CreateDW –SQL script file to create star-schema for DW /30
The script should create all dimension and fact tables table in DW and if any table with same name already exists, the table should be droped. It should also apply all primary and foreign keys on the right attributes.

Usually in case of star-schema for sales the dimension tables are: product, date, store, and supplier while the fact table is sales

Implementing of INLJ /30
INLJ procedure should implement all three phases of ETL – it should extract records from TRANSACTION table, transform these with MD and then load these records to DW successfully.

queriesDW – SQL script file containing of all your OLAP queries /15
The file should include OLAP queries for all tasks presented in Section 7.

projectReport – a doc file containing all contents described in point 4 under the task break-up section. /15
Report must contain project overview, INLJ algorithm, schema for DW, your OLAP queries with outputs and a summary of what was learnt from the project.

readMe – a text file describing the step-by-step instructions to operate your project /5
readMe file should contain a step-by-step guide to operate the project.

Late submission penalty -/5
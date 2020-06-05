How to run this project:

Requires:

- All SQL file run in Oracle SQL Developer with connection to msdbs server. 
- TRANSACTIONS & MASTERDATA tables have been created by scripts provided in this assessment.

Steps:

1. Run script createDW.sql. It creates all tables needed for star-schema of DW,
   (Drop old ones first if any), and displays basic information of tables just created.
2. Run INLJ.sql, which reads data from TRANSACTIONS & MASTERDATA tables, do transformation,
   and insert into DW tables.
3. Run queriesDW.sql, which do the queries.

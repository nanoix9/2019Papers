---
documentclass: article
title: |
    ```{=latex}
        \textbf{COMP810 Data Warehousing and Big Data \\
        Assessment 2 Data Warehousing Project}
    ```
subtitle: "Building and Analysing a DW for NatureFresh Stores in NZ"
author: "Stone Fang (Student ID: 19049045)" 
header: "COMP810 Data Warehousing and Big Data Assessment 2"
footer: "Stone Fang (19049045)"
pagestyle: "empty"
# biblio-style: apa
# biblio-title: References
# bibliography: [dl.bib]
# biblatexoptions:
    # - backend=biber
papersize: a4
# fontsize: 12pt
linestretch: 1.25
geometry:
    - margin=25mm
graphics: true

header-includes:
    - \fancypagestyle{plain}{\pagestyle{fancy}}
    # - \renewcommand*\familydefault{\sfdefault}
    # - \usepackage{bm}
    # - \usepackage{tikz}
    # - \renewcommand{\sfdefault}{phv}
    # - \renewcommand{\sfdefault}{pag}
    # - \renewcommand{\familydefault}{ppl}
    # - |
    #     ```{=latex}
    #         \makeatletter
    #         \patchcmd{\@verbatim}
    #             {\verbatim@font}
    #             {\verbatim@font\small}
    #             {}{}
    #         \makeatother
    #     ```
    - |
        ```{=latex}
            \usepackage{tcolorbox}

            \newcommand{\sqloutputbegin}[1][SQL Output]{
                \hspace{0.5cm}
                \begin{minipage}[c]{0.93\linewidth} 
                \centering
                \begin{tcolorbox}[colback=gray!8, colframe=white,
                    boxrule=0pt, coltitle=black,
                    colbacktitle=gray!15, title={#1}]
                \centering
                \small}
            \newcommand{\sqloutputend}{
                \end{tcolorbox} 
                \end{minipage}}
        ```

# fontfamily: ptsans
# fontfamily: txfonts
fontfamily: mathpazo
# fontfamily: newtxtext,newtxmath
# fontfamily: FiraSans
# fontfamilyoptions: sfdefault
# fontfamily: newtxsf
# fontfamily: mathdesign
# fontfamilyoptions: utopia
# fontfamily: helvet 
# fontfamily: tgheros
# fontfamily: kpfonts
# fontfamily: libertine
# fontenc: T1
# fontfamily: tgadventor
# fontfamily: gfsdidot
# fontfamily: mathptmx,tgtermes
# fontfamily: beton,euler
# fontenc: T1
# fontfamily: concmath
# fontenc: T1
# fontfamily: droidserif
# fontfamilyoptions: default
# fontenc: T1
# fontfamily: electrum
# fontfamilyoptions: lf
# fontenc: T1
# fontfamily: eulervm
# fontfamilyoptions: [euler-digits, small]

---

# Project Overview

The goal of this project is to create a Data Warehouse (DW) for the sales analysis of NatureFresh, 
one of the largest fresh food market chains in New Zealand. Analysis of sales 
and customer shopping behaviours can give NatureFresh in-depth insight of the market,
so they can improve their selling strategies accordingly.

The original available data are customer transactions and product information.
The transaction data contains records of customer buying, including who (customer)
bought what (product), when (date), where(store) and how many was bought (quantity).
The product data contains information for each product, including supplier and price.

However, the format of original data doesn't fit into the requirement of OLAP,
so first we need transform the data into other formats for better querying.

The major content of this project contains:

- Design and implement the star-schema for sales DW, i.e. fact & dimension tables
- Fill DW by ETL process. Specifically, do Index Nested Loop Join (INLJ) on
    transactions and master data, transform and load data into fact & dimension tables.
- Execute queries on DW

All the operations above are implemented in SQL.

# Schema for DW

According to the original data, the DW will consist of one fact table *Sales* 
and five dimension tables *Product*, *Supplier*, *Customer*, *Store*, and *Date*,
as shown in Figure \ref{fig:overall}. The SQL code to create all tables are
in file *createDW.sql*.

\begin{figure}[htbp]
  \centering
  % \sffamily
  {
  %\fontfamily{phv}\selectfont
  \fontsize{9}{10}\selectfont
  % \fontsize{7}{7}\selectfont
  \def\svgwidth{0.9\columnwidth}
    \resizebox{0.9\textwidth}{!}{\input{star-schema.pdf_tex}}
  }
  \caption{Star Schema of NatureFresh Sales}
  \label{fig:overall}
\end{figure}


## Fact Table

Apparently the fact table should have foreign keys corresponding to all five dimension
tables, and the quantity of item sold. There are two decisions have been make
for primary key and amount of money in sales.

**Primary key** of fact table can be a combination of all foreign keys. However,
there could be a concern to have more than one transactions for the same values on all five
dimensions. A quick analysis shows that such situation does exists, though the possibility is low. 
In other words, a customer may buy one product multiple times 
at one store in one day. There are two options to solve this problem. One is
summing up the quantities of multiple transactions, resulting in only one record
for the same combination of dimension values. The other is keep multiple transactions
while use a separated ID field as the primary key of *Sales* fact table. 
In this project, the latter solution is preferred because this approach can keep
the original granularity of transactions, thus contains more information. 
Also, the possibility of multiple transactions for one combination of dimensions
is low, so there would not be significant overhead in terms of memory and storage.

**Price/Amount** is another concerning field. In the original data,
*price* is stored in master data table as a property of product, so it is natural
to make it an attribute of product dimension. However, this design has a 
shortcoming when price changes as it always does. If the price of a product changes,
we can't simply modify the value in *Product* dimension table otherwise the result
on sales before that change will be incorrect. Therefore, in this project price 
information is kept in *Sales* table. Since the amount of money in sales
is a more frequent used number, we add to fact table an *amount* filed which 
is calculated by $\mathit{quantity}\times \mathit{price}$. 
In section \ref{price-attribute} further discussions will be provided on this issue.

## Dimensions

Details of dimension tables can be referred to Figure \ref{fig:overall}. 
Most dimensions are as simple as "ID+name", while the *Date* dimension is relatively
complicated. First of all, unlike other dimensions, there is no existing ID for *Date*.
In this project, a string in format of "YYYYMMDD" is chosen as the ID for *Date*, 
rather than an auto-incremental column. The advantage is such ID is more readable
and intuitive, and thus more convenient for partitioning if required in the future.
On the other hand, it would need more storage space, which, however, is not a big
issue providing the cost storage is quite low nowadays. Second, *Date* dimension
contains more information other than names. In this project, common properties
are calculated, including *year*, *quarter*, *month*, *week*, *day*, *day_of_week*.
In fact, it can be extended to more fields such as *is_public_holiday*, if some
analysis on holiday is in demand.

# INLJ Algorithm

Index Nested Loop Join (INLJ) is a table joining algorithm that can be used for
stream data joining. Nested Loop Join takes an outer loop and an inner loop, each
for one table, and output the rows that matches the conditions, so the time complexity
is $O(N M)$ where $N$ and $M$ are the number of rows of two tables.
. However, INLJ only keep the outer loop and replace the inner loop with an index-based
loop up, thus greatly reduce the time complexity. For example, if the index is
implemented by B-tree, then complexity of lookup is a logarithm of $M$ 
instead of linear which is the case of the inner loop.

This algorithm is implemented in PL/SQL. First, a bulk (50 rows in this project) 
of transactions are read into memory. 
Then all rows in the bulk are read one after another, and retrieve 
the information for current row from master data by *product_id*. 
Then all properties corresponding to current row are transformed to fit the 
star schema and then load into the fact and dimension tables. Please refer to
file *INLJ.sql* for the complete implementation.

# OLAP Queries Results

This section summarise the results of required analysis. The SQL statements
for these queries are referred to file *queriesDW.sql*.

\let\oldsubsection\thesubsection
\renewcommand*{\thesubsection}{Question~\arabic{subsection}}

## 
<!-- Top 5 products in Dec 2019 -->

> Determine the top 5 products in Dec 2019 in terms of total sales

\sqloutputbegin

    PRODUCT_NAME                   TOTAL_SALES       RANK
    ------------------------------ ----------- ----------
    Bouillon cubes                     1759.58          1
    Kiwis                              1757.75          2
    Mac and cheese                        1632          3
    Relish                             1574.18          4
    Pears                              1396.53          5

\sqloutputend

## 
<!-- Store producing highest sales -->

> Determine which store produced highest sales in the whole year?

\sqloutputbegin

    STORE_NAME           TOTAL_SALES       RANK
    -------------------- ----------- ----------
    Manukau                 82873.81          1

\sqloutputend

## 
<!-- Top 3 products for three consecutive months -->

> Determine the top 3 products for a month (say, Dec 2019), and 
for the 2 months before that, in terms of total sales.

\sqloutputbegin

    PRODUCT_NAME                   TOTAL_SALES       RANK      MONTH       YEAR
    ------------------------------ ----------- ---------- ---------- ----------
    Bouillon cubes                     1759.58          1         12       2019
    Kiwis                              1757.75          2         12       2019
    Mac and cheese                        1632          3         12       2019
    Onions                             2296.74          1         11       2019
    Relish                             1751.91          2         11       2019
    Broccoli                           1514.52          3         11       2019
    Paprika                             1692.6          1         10       2019
    Pizza / Pizza Rolls                   1505          2         10       2019
    Oregano                             1476.8          3         10       2019

\sqloutputend

## 
<!-- Product-wise materialised view -->

> Create a materialised view called “STOREANALYSIS” that presents 
the product-wise sales analysis for each store. The results should be ordered 
by StoreID and then ProductID.

<!-- STOREID PRODUCTID SUM(STORE_TOTAL) 
-------- ---------- ---------------- -->

\sqloutputbegin[SQL Output\footnotemark]

    STOR PRODUC TOTAL_SALES
    ---- ------ -----------
    S-1  P-1001       540.9
    S-1  P-1002       164.4
    S-1  P-1003      448.76
    S-1  P-1004       250.2
    S-1  P-1005     1318.68

\sqloutputend

\footnotetext{
The output from Oracle SQL Developer doesn't show the complete names of columns,
which I assume is a feature on materilised view to save display areas.
It's only a sample query for inspection of the materialised view which has been 
just created. The content is correct, so the output was just copied and 
pasted here without any manual editing.
}

## 
<!-- Further analysis on materialised view -->

> Think about what information can be retrieved from the materialised view
> created in Q4 using ROLLUP or CUBE concepts and provide some useful information
> of your choice for management.

\renewcommand*{\thesubsection}{\oldsubsection}

# Discussion

## Price Attribute

In this design, the price information is beared in the *amount* field of 
fact table because of the fact that prices of products are subject to change.
However, changes of prices are way less frequent than transactions, so there will
be much redundant storage for price information. An alternative design is to
add an extra dimension *SellingItem* which is simply a combination of *Product*
and *price*. When price changes, a new "selling item" will be created with 
the same *product_id* and the new *price*. This method is show in 
Figure \ref{fig:alter-price}. The benefit is reducing the required storage
for price by normalisation. However, this alternative design ends up with an 
architecture other than star-schema.

\begin{figure}[htbp]
  \centering
  % \sffamily
  {
  %\fontfamily{phv}\selectfont
  \fontsize{10}{11}\selectfont
  % \fontsize{7}{7}\selectfont
  %\def\svgwidth{0.9\textwidth}
    \resizebox{0.85\textwidth}{!}{\input{alternative-price-attr.pdf_tex}}
  }
  \caption{Alternative Design for Price Attribute}
  \label{fig:alter-price}
\end{figure}


# Summary of Learning Outcomes


## DW Development Lifecycle

The first and foremost thing I learned is how to develop a DW through the 
whole lifecycle. It involves requirement analysis, schema design, data ETL,
and querying. We need to divide this complex task into different stages,
and also be able to combine them together back into a complete and running
DW project. 

## DW Schema

The DW is usually modelled as data cube which consists of dimensions and measurements. 
In terms of physical model, dimensions are mapped to dimension tables and
measurements are mapped to fact tables.
There are two major schema for DW design, star-schema and snowflake schema.
In this project we use star-schema, which is more efficient for querying 
because it has less table joints for a query. However, the disadvantage is
the lack of normalisation. 
Most dimensions are simple, containing only one 
attributed of "name". However, the *Date* dimension is trickier. 

## INLJ & ETL

INLJ is suitable for joining stream data with batch data in near real-time.

## DW Query & Analysis

Analysis on DW should be translated to SQL queries. It's usually required 
to do table join so the query would be a bit complicated even for a simple analysis.

**Top K retrieval** is a type of common analysis, which finds the most or
least measurements with corresponding dimension values. For example, it's useful
for decision-making in business operation
to know the products with K highest or lowest sales. This can be done by 
either `ORDER BY` or `RANK()` operations in Oracle SQL Developer. More than that,
the analytics are usually done with roll-up/drill-down/slice/dice operations.
For instance, it's common to aggregate the data of each day to month level (roll-up),
or retrieve data of a certain month (slice) or a month range (dice). 
For this purpose, the `WHERE` and `GROUP BY` clause are used, sometimes
with `PARTITION BY` operation for advanced query.

**Dynamic query** is an important way to improve flexibility and query reuse. 
Dynamic query is constructed in runtime with parameters substituted by
real values assigned to them. Next time if we want to do similar analysis, we
just need to change the parameter rather than manually editing the query statement.
To implement a dynamic query is basically to create a PL/SQL table function with 
the query wrapped inside it. It's called "table function" because it returns
collections of objects that minic tables. However, the details are somewhat complicated.
What I learned from developing a dynamic query includes:

- Create types of expected table for return type declaration in function
    by `CREATE TYPE`. 
- In side the function, create a parameterised cursor for data fetching.
    The parameters are about the target month, so the query can be used
    to select data of any specified month.
- Use `FOR LOOP` and `IF THEN ELSE` to iteractively fetch data from database,
    and convert the retrieved data into the type matching the function declaration.
- Use `PIPELINED` and `PIPE ROW` together to return the fetched records in 
    an convenient way. Without this approach we would have to create a local
    collection, append records to it and return it after all data has been retrieved,
    but with `PIPELINED` we can simply "pipe" out each record immediately after
    it's retrieved without the needs for local collection.
    

## SQL & Oracle Developer

In this project a lot of SQL knowledge has been learned. Other than basic

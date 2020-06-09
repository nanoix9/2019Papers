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









PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Bouillon cubes                     1759.58          1
Kiwis                              1757.75          2
Mac and cheese                        1632          3
Relish                             1574.18          4
Pears                              1396.53          5
English muffins                    1383.79          6
Pasta                               1296.3          7
Corn                               1294.26          8
Onions                             1182.48          9
Celery                             1175.94         10
Fish sticks                        1147.55         11

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Pizza / Pizza Rolls                   1120         12
Applesauce                         1108.85         13
Lemon / Lime juice                  1063.8         14
Peaches                            1046.07         15
Paprika                             1019.2         16
Broccoli                           1009.68         17
Melon                              1008.15         18
Tomatoes                           1006.38         19
Pancake / Waffle mix                983.24         20
Breakfasts                          982.17         21
Black pepper                           980         22

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Grapefruit                          955.34         23
Lettuce / Greens                    934.08         24
Cereal                               922.2         25
Vegetables                          910.12         26
Tofu                                907.73         27
Garlic                              905.25         28
Cilantro                            863.36         29
Cauliflower                         845.74         30
Tinned meats                        812.15         31
Soups                               811.44         32
Squash                              799.24         33

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Mint                                763.98         34
Gravy                               741.12         35
Ginger                                 738         36
Salad dressing                      711.54         37
Peppers                             703.36         38
Burritos                            703.04         39
Peanut butter                       695.76         40
Lemons / Limes                      684.23         41
Steak sauce                         673.64         42
Mushrooms                              666         43
Cherries                            650.18         44

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Tea                                 639.36         45
Apples                              603.52         46
Hot sauce                           585.99         47
Soy sauce                            563.5         48
Mayonnaise                          555.84         49
Olive oil                           550.44         50
Oregano                              540.8         51
Pasta sauce                         506.92         52
Grapes                              495.39         53
Basil                               477.66         54
Chili                               462.13         55

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Tuna / Chicken                      445.48         56
Spinach                             442.35         57
TV dinners                           418.6         58
Ready-bake breads                   414.18         59
Fruit juice                         390.78         60
Bagels                               366.3         61
Salsa                               347.33         62
Bananas                             346.95         63
Fruit                               343.98         64
Juice concentrate                    336.2         65
Vegetable oil                       310.98         66

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Chip dip                             307.6         67
Asparagus                           299.25         68
Baked beans                          286.8         69
Ketchup / Mustard                    274.4         70
Cucumbers                           269.44         71
Vinegar                                243         72
Instant potatoes                    237.65         73
Hummus                              236.08         74
Avocados                            230.36         75
Worcestershire sauce                 229.1         76
Plums                               207.06         77

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Eggs / Fake eggs                    201.81         78
Berries                             199.64         79
Veggie burgers                      193.96         80
Nectarines                           191.1         81
BBQ sauce                           184.32         82
Tortillas                           160.42         83
Popsicles                           160.32         84
Carrots                             153.44         85
Cinnamon                            151.92         86
Potatoes                            146.88         87
Veggies                             135.08         88

PRODUCT_NAME                   TOTAL_SALES       RANK
------------------------------ ----------- ----------
Oranges                             115.05         89
Parsley                              105.1         90
Syrup                                89.24         91
Coffee / Filters                     88.38         92
Honey                                83.98         93
Rice                                 80.08         94
Jam / Jelly / Preserves              79.55         95
Ice cream / Sorbet                   76.35         96
Fries / Tater tots                   68.37         97
Olives                               36.27         98
Pickles                              36.14         99

99 rows selected. 


STORE_NAME           TOTAL_SALES       RANK
-------------------- ----------- ----------
Manukau                 82873.81          1
Westgate                82771.26          2
Albany                  80560.02          3
Whangaparaora           80559.21          4
St. james               78686.72          5
East Auckland           78219.92          6
West Auckland           76360.63          7
Massey                  74629.76          8
Henderson                42562.6          9
Queen St.               40450.26         10

10 rows selected. 


PRODUCT_NAME                   TOTAL_SALES       RANK      MONTH EXTRACT(YEARFROMT_DATE)
------------------------------ ----------- ---------- ---------- -----------------------
Bouillon cubes                     1759.58          1         12                    2019
Kiwis                              1757.75          2         12                    2019
Mac and cheese                        1632          3         12                    2019
Onions                             2296.74          1         11                    2019
Relish                             1751.91          2         11                    2019
Broccoli                           1514.52          3         11                    2019
Paprika                             1692.6          1         10                    2019
Pizza / Pizza Rolls                   1505          2         10                    2019
Oregano                             1476.8          3         10                    2019

9 rows selected. 


STORE_NAME           PRODUCT_NAME                   TOTAL_SALES       RANK
-------------------- ------------------------------ ----------- ----------
Albany                                                 80560.02          1
Albany               Soups                              2328.48          2
East Auckland                                          78219.92          1
East Auckland        Oregano                               2080          2
Henderson                                               42562.6          1
Henderson            Burritos                           1713.66          2
Manukau                                                82873.81          1
Manukau              Corn                                  2442          2
Massey                                                 74629.76          1
Massey               Bouillon cubes                     2031.68          2
Queen St.                                              40450.26          1

STORE_NAME           PRODUCT_NAME                   TOTAL_SALES       RANK
-------------------- ------------------------------ ----------- ----------
Queen St.            Corn                               1318.68          2
St. james                                              78686.72          1
St. james            Celery                             2201.76          2
West Auckland                                          76360.63          1
West Auckland        Celery                                2502          2
Westgate                                               82771.26          1
Westgate             Melon                               2946.9          2
Whangaparaora                                          80559.21          1
Whangaparaora        Mac and cheese                      2320.5          2
                                                      717674.19          1

21 rows selected. 

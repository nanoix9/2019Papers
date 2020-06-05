SELECT count(*) FROM Product;
SELECT * FROM Store;
SELECT * FROM Supplier;
SELECT count(*) FROM Customer;
SELECT count(*) FROM DateDim;
SELECT * FROM Customer WHERE ROWNUM < 100;
SELECT * FROM DateDim WHERE ROWNUM < 100;
SELECT * FROM Sales WHERE ROWNUM < 100;
SELECT count(*) FROM Sales WHERE ROWNUM < 100;

select SUPPLIER_ID, WM_CONCAT(DISTINCT SUPPLIER_NAME) FROM MASTERDATA group by SUPPLIER_ID;
select SUPPLIER_ID, COUNT(DISTINCT SUPPLIER_NAME) FROM MASTERDATA group by SUPPLIER_ID;

select product_name, sum(quantity * price) ts
from TRANSACTIONS t
join MASTERDATA m
on t.product_id = m.product_id
where extract(month from t_date) = 12
group by product_name
order by ts desc;

SELECT * FROM dual;


-- 1167	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1086' and customer_id='C-19' and	store_id='S-2' and t_date=DATE'2019-07-08'; --	8	96.32
-- 1168	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1006' and customer_id='C-27' and	store_id='S-5' and t_date=DATE'2019-07-19'; --	6	50.52
-- 1169	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1037' and customer_id='C-34' and	store_id='S-8' and t_date=DATE'2019-12-28'; --	7	147.77
-- 1170	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1098' and customer_id='C-44' and	store_id='S-8' and t_date=DATE'2019-12-28'; --	3	54.6
-- 1171	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1003' and customer_id='C-14' and	store_id='S-4' and t_date=DATE'2019-05-05'; --	4	69.04
-- 1172	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1079' and customer_id='C-35' and	store_id='S-7' and t_date=DATE'2019-05-17'; --	9	81
-- 1173	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1008' and customer_id='C-20' and	store_id='S-6' and t_date=DATE'2019-01-28'; --	7	93.24
-- 1174	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1035' and customer_id='C-31' and	store_id='S-2' and t_date=DATE'2019-09-30'; --	6	54.48
-- 1175	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1088' and customer_id='C-22' and	store_id='S-7' and t_date=DATE'2019-09-02'; --	5	97
-- 1176	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1086' and customer_id='C-7	' andSstore_id='-2	' and t_date=DATE'0190-42-7	'; --10	120.4
-- 1177	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1023' and customer_id='C-9	' andSstore_id='-5	' and t_date=DATE'0190-20-7	'; --5	64.55
-- 1178	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1050' and customer_id='C-37' and	store_id='S-8' and t_date=DATE'2019-04-26'; --	3	30.72
-- 1179	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1057' and customer_id='C-24' and	store_id='S-9' and t_date=DATE'2019-08-16'; --	6	52.44
-- 1180	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1052' and customer_id='C-17' and	store_id='S-4' and t_date=DATE'2019-05-07'; --	5	16.15
-- 1181	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1062' and customer_id='C-24' and	store_id='S-2' and t_date=DATE'2019-11-17'; --	9	137.79
-- 1182	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1010' and customer_id='C-34' and	store_id='S-5' and t_date=DATE'2019-03-17'; --	7	87.92
-- 1183	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1029' and customer_id='C-35' and	store_id='S-8' and t_date=DATE'2019-08-08'; --	1	9.86
-- 1184	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1086' and customer_id='C-43' and	store_id='S-3' and t_date=DATE'2019-08-01'; --	10	120.4
-- 1185	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1019' and customer_id='C-40' and	store_id='S-7' and t_date=DATE'2019-04-30'; --	3	51.33
-- 1186	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1023' and customer_id='C-2	' andSstore_id='-10' and t_date=DATE'2019-03-14'; --	8	103.28
-- 1187	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1003' and customer_id='C-30' and	store_id='S-6' and t_date=DATE'2019-12-12'; --	9	155.34
-- 1188	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1065' and customer_id='C-5	' andSstore_id='-2	' and t_date=DATE'0190-31-7	'; --7	126.98
-- 1189	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1030' and customer_id='C-21' and	store_id='S-5' and t_date=DATE'2019-08-10'; --	8	32.56
-- 1190	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1082' and customer_id='C-26' and	store_id='S-7' and t_date=DATE'2019-06-30'; --	3	37.47
-- 1191	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1014' and customer_id='C-16' and	store_id='S-2' and t_date=DATE'2019-07-14'; --	8	14.32
-- 1192	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1059' and customer_id='C-34' and	store_id='S-3' and t_date=DATE'2019-02-11'; --	2	21.24
-- 1193	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1063' and customer_id='C-21' and	store_id='S-1' and t_date=DATE'2019-03-27'; --	7	13.58
-- 1194	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1045' and customer_id='C-28' and	store_id='S-9' and t_date=DATE'2019-04-05'; --	3	20.04
-- 1195	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1035' and customer_id='C-27' and	store_id='S-7' and t_date=DATE'2019-11-19'; --	6	54.48
-- 1196	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1087' and customer_id='C-30' and	store_id='S-2' and t_date=DATE'2019-02-27'; --	7	123.48
-- 1197	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1038' and customer_id='C-10' and	store_id='S-4' and t_date=DATE'2019-05-04'; --	3	18.51
-- 1198	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1020' and customer_id='C-20' and	store_id='S-3' and t_date=DATE'2019-07-19'; --	10	258.2
-- 1199	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1068' and customer_id='C-12' and	store_id='S-6' and t_date=DATE'2019-11-05'; --	9	43.65
-- 1200	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1018' and customer_id='C-3	' andSstore_id='-1	' and t_date=DATE'0190-12-2	'; --1	3.22
-- 1201	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1049' and customer_id='C-38' and	store_id='S-3' and t_date=DATE'2019-11-07'; --	2	14.92
-- 1202	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1025' and customer_id='C-44' and	store_id='S-8' and t_date=DATE'2019-06-01'; --	10	29.5
-- 1203	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1087' and customer_id='C-20' and	store_id='S-4' and t_date=DATE'2019-06-30'; --	5	88.2
-- 1204	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1084' and customer_id='C-35' and	store_id='S-5' and t_date=DATE'2019-06-09'; --	3	3.51
-- 1205	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1002' and customer_id='C-27' and	store_id='S-2' and t_date=DATE'2019-12-12'; --	2	10.96
-- 1206	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1039' and customer_id='C-22' and	store_id='S-7' and t_date=DATE'2019-01-25'; --	7	109.13
-- 1207	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1010' and customer_id='C-32' and	store_id='S-9' and t_date=DATE'2019-08-27'; --	6	75.36
-- 1208	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1011' and customer_id='C-13' and	store_id='S-3' and t_date=DATE'2019-08-04'; --	7	32.13
-- 1209	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1056' and customer_id='C-18' and	store_id='S-6' and t_date=DATE'2019-06-05'; --	5	38.6
-- 1210	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1011' and customer_id='C-34' and	store_id='S-3' and t_date=DATE'2019-09-12'; --	4	18.36
-- 1211	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1028' and customer_id='C-11' and	store_id='S-6' and t_date=DATE'2019-01-30'; --	10	236.7
-- 1212	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1019' and customer_id='C-42' and	store_id='S-7' and t_date=DATE'2019-03-31'; --	2	34.22
-- 1213	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1011' and customer_id='C-27' and	store_id='S-4' and t_date=DATE'2019-07-10'; --	6	27.54
-- 1214	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1005' and customer_id='C-48' and	store_id='S-7' and t_date=DATE'2019-08-10'; --	2	48.84
-- 1215	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1045' and customer_id='C-19' and	store_id='S-8' and t_date=DATE'2019-01-02'; --	6	40.08
-- 1216	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1028' and customer_id='C-2	' andSstore_id='-8	' and t_date=DATE'0190-12-1	'; --8	189.36
-- 1217	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1096' and customer_id='C-39' and	store_id='S-9' and t_date=DATE'2019-05-06'; --	7	157.29
-- 1218	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1076' and customer_id='C-32' and	store_id='S-7' and t_date=DATE'2019-11-07'; --	8	29.12
-- 1219	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1047' and customer_id='C-19' and	store_id='S-7' and t_date=DATE'2019-09-14'; --	3	62.79
-- 1220	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1018' and customer_id='C-48' and	store_id='S-6' and t_date=DATE'2019-06-22'; --	2	6.44
-- 1221	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1087' and customer_id='C-37' and	store_id='S-7' and t_date=DATE'2019-02-25'; --	4	70.56
-- 1222	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1006' and customer_id='C-41' and	store_id='S-6' and t_date=DATE'2019-05-12'; --	1	8.42
-- 1223	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1011' and customer_id='C-32' and	store_id='S-5' and t_date=DATE'2019-03-19'; --	5	22.95
-- 1224	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1081' and customer_id='C-13' and	store_id='S-1' and t_date=DATE'	201-90-41'; --4	5	35.85
-- 1225	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1073' and customer_id='C-38' and	store_id='S-1' and t_date=DATE'	201-90-13'; --0	8	178.8
-- 1226	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1001' and customer_id='C-30' and	store_id='S-7' and t_date=DATE'2019-03-07'; --	2	36.06
-- 1227	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1090' and customer_id='C-6	' andSstore_id='-6	' and t_date=DATE'0191-20-8	'; --9	75.42
-- 1228	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1055' and customer_id='C-7	' andSstore_id='-8	' and t_date=DATE'0190-52-7	'; --2	9.8
-- 1229	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1020' and customer_id='C-34' and	store_id='S-4' and t_date=DATE'2019-12-16'; --	1	25.82
-- 1230	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1045' and customer_id='C-42' and	store_id='S-9' and t_date=DATE'2019-07-09'; --	5	33.4
-- 1231	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1016' and customer_id='C-21' and	store_id='S-4' and t_date=DATE'2019-03-19'; --	2	17.72
-- 1232	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1059' and customer_id='C-25' and	store_id='S-3' and t_date=DATE'2019-02-27'; --	6	63.72
-- 1233	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1057' and customer_id='C-45' and	store_id='S-7' and t_date=DATE'2019-04-09'; --	10	87.4
-- 1234	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1083' and customer_id='C-29' and	store_id='S-6' and t_date=DATE'2019-10-06'; --	9	63.18
-- 1235	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1015' and customer_id='C-17' and	store_id='S-7' and t_date=DATE'2019-06-26'; --	5	36.8
-- 1236	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1067' and customer_id='C-39' and	store_id='S-8' and t_date=DATE'2019-07-16'; --	4	58.92
-- 1237	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1032' and customer_id='C-5	' andSstore_id='-2	' and t_date=DATE'0190-50-6	'; --4	77.96
-- 1238	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1012' and customer_id='C-14' and	store_id='S-1' and t_date=DATE'2019-07-14'; --	2	19.66
-- 1239	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1023' and customer_id='C-33' and	store_id='S-7' and t_date=DATE'2019-12-22'; --	4	51.64
-- 1240	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1075' and customer_id='C-33' and	store_id='S-9' and t_date=DATE'2019-10-17'; --	8	11.12
-- 1241	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1012' and customer_id='C-36' and	store_id='S-3' and t_date=DATE'2019-09-03'; --	10	98.3
-- 1242	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1098' and customer_id='C-41' and	store_id='S-2' and t_date=DATE'2019-11-20'; --	7	127.4
-- 1243	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1072' and customer_id='C-39' and	store_id='S-4' and t_date=DATE'2019-06-24'; --	9	188.28
-- 1244	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1058' and customer_id='C-10' and	store_id='S-9' and t_date=DATE'2019-05-25'; --	6	152.34
-- 1245	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1045' and customer_id='C-34' and	store_id='S-3' and t_date=DATE'2019-01-01'; --	9	60.12
-- 1246	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1006' and customer_id='C-34' and	store_id='S-4' and t_date=DATE'2019-03-30'; --	3	25.26
-- 1247	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1093' and customer_id='C-29' and	store_id='S-6' and t_date=DATE'2019-08-28'; --	10	84.4
-- 1248	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1041' and customer_id='C-4	' andSstore_id='-10' and t_date=DATE'2019-05-04'; --	3	58.35
-- 1249	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1042' and customer_id='C-48' and	store_id='S-8' and t_date=DATE'2019-04-04'; --	6	152.7
-- 1250	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1018' and customer_id='C-27' and	store_id='S-8' and t_date=DATE'2019-07-25'; --	8	25.76
-- 1251	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1096' and customer_id='C-10' and	store_id='S-6' and t_date=DATE'2019-04-01'; --	8	179.76
-- 1252	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1043' and customer_id='C-29' and	store_id='S-9' and t_date=DATE'2019-09-25'; --	3	24.6
-- 1253	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1054' and customer_id='C-2	' andSstore_id='-7	' and t_date=DATE'0191-02-9	'; --4	8.6
-- 1254	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1067' and customer_id='C-37' and	store_id='S-4' and t_date=DATE'2019-11-23'; --	3	44.19
-- 1255	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1038' and customer_id='C-18' and	store_id='S-9' and t_date=DATE'2019-10-25'; --	8	49.36
-- 1256	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1024' and customer_id='C-13' and	store_id='S-8' and t_date=DATE'2019-03-07'; --	5	129.25
-- 1257	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1064' and customer_id='C-22' and	store_id='S-5' and t_date=DATE'2019-03-20'; --	5	14.5
-- 1258	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1087' and customer_id='C-18' and	store_id='S-2' and t_date=DATE'2019-02-04'; --	7	123.48
-- 1259	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1007' and customer_id='C-15' and	store_id='S-1' and t_date=DATE'	201-91-11'; --8	1	19.46
-- 1260	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1077' and customer_id='C-17' and	store_id='S-6' and t_date=DATE'2019-12-06'; --	5	59.2
-- 1261	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1008' and customer_id='C-37' and	store_id='S-2' and t_date=DATE'2019-12-11'; --	6	79.92
-- 1262	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1070' and customer_id='C-47' and	store_id='S-9' and t_date=DATE'2019-06-30'; --	10	255
-- 1263	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1092' and customer_id='C-49' and	store_id='S-4' and t_date=DATE'2019-05-19'; --	5	60.8
-- 1264	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1065' and customer_id='C-25' and	store_id='S-1' and t_date=DATE'2019-09-15'; --	5	90.7
-- 1265	
SELECT t.*, m.*, quantity * price FROM TRANSACTIONS t INNER JOIN MASTERDATA m ON t.product_id = m. product_id WHERE t.product_id='P-1064' and customer_id='C-21' and	store_id='S-7' and t_date=DATE'2019-12-19'; --	2	5.8
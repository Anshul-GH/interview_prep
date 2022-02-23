TABLE_1		TABLE_2
		
COLUMN_1	COLUMN_2
1		0
1		1
0		1
0		2
2		4
3		null
null		null
null		null

What will be the output of the following query:

SELECT count(*)
FROM TABLE_1 LEFT JOIN TABLE_2
ON TABLE_1.COLUMN_1 = TABLE_2.COLUMN_2;"
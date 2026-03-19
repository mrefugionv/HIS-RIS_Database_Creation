SELECT {agg / classificacion} (col 1 )  {particion} AS name
FROM table1
LEFT/ FULL/ RIGHT/ INNER JOIN table2 ON table1.col = table2 .col
WHERE table#.col {comparacion} table#.col     *no agg
GROUP BY col
GAVING {agg} col  {comparacion} value
ORDER BY col DESC/ASC
LIMIT #filas

{agg} = MIN , MAX, SUM, DISTINCT, COUNT, AVG
{classificacion} = RANK, ROW_NUMBER, LAG. LEAD, FIRST VALUE, LAST VALUE
{paticion}= OVER( PARTITION BY col2
                ORDER BY  col2
                ROW BETWEEN <start_bound> AND <end_bound>)
<baound> = UNBOUNDED PRECEDING/ FOLLOWING, N PRECEDING / FOLLOWING, CURRENT ROW
{comparcion} =  >, < , >= , <=, ...
 
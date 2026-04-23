# SQL QUERY COMMANDS
[[_LOC_]]

Pre-process the data as much as possible before the app processes it (for example, using a sum instead of for loops or similar constructs in other programming languages).

There two main types of SQL querying:

| Feature          | GROUP BY 🧱 | Window Functions 🌊 |
| ------------------ | ----------- | ------------------- |
| ¿Reduce rows?     | Yes          | No                  |
| ¿Details remain? | No          | Yes                  |
| ¿HAVING?       | Yes          | No     |
| ¿OVER()?       | No          | Yes                |


## GROUP BY QUERYING 

```
SELECT col_no_agg, AGG(col) AS 'new_col_name'
FROM table1
JOIN table2 ON table1.col = table2 .col
GROUP BY col_no_agg
HAVING {CONDITION} [AGG(col) > value] 
ORDER BY col DESC/ASC
LIMIT #rows; 
```


## WINDOW QUERYING

```
SELECT col_no_agg, ... ,..., WINDOW(col) OVER (PARTITION BY col2
                ORDER BY  col3
                ROW BETWEEN {start_bound} AND {end_bound}) AS 'new_col_name'
FROM table1
JOIN table2 ON table1.col = table2 .col
WHERE {CONDITION}[table#.col {COMP} value {LOGIC} table#.col {COMP} value]
ORDER BY col DESC/ASC
LIMIT #rows ; 
```
## WINDOW FILTERING
```
SELECT *
FROM (
  SELECT WINDOW(col) OVER (PARTITION BY col2
                ORDER BY  col3
                ROW BETWEEN {start_bound} AND {end_bound}) AS 'new_col_name'
  FROM table1
) result_alias
WHERE 'new_col_name' = 1;
```
####  CASE EXAMPLE

Having the table "sales"

| id | salesperson | region | amount |
| -- | -------- | ------ | ----- |
| 1  | Ana      | Norte  | 100   |
| 2  | Ana      | Norte  | 200   |
| 3  | Ana      | Sur    | 150   |
| 4  | Luis     | Norte  | 300   |
| 5  | Luis     | Sur    | 100   |
| 6  | Luis     | Sur    | 200   |

1. Group by - to obtain total amount sold by each salesperson

```
SELECT vendedor, SUM(monto) AS total
FROM ventas
GROUP BY vendedor;
```
| vendedor | total |
| -------- | ----- |
| Ana      | 450   |
| Luis     | 600   |

2. Window function - obtain the total amount sold by each person but without lossing the information.

```
SELECT 
    id,
    vendedor,
    region,
    monto,
    SUM(monto) OVER (PARTITION BY vendedor) AS total_vendedor
FROM ventas;
```
| id | vendedor | region | monto | total_vendedor |
| -- | -------- | ------ | ----- | -------------- |
| 1  | Ana      | Norte  | 100   | 450            |
| 2  | Ana      | Norte  | 200   | 450            |
| 3  | Ana      | Sur    | 150   | 450            |
| 4  | Luis     | Norte  | 300   | 600            |
| 5  | Luis     | Sur    | 100   | 600            |
| 6  | Luis     | Sur    | 200   | 600            |

3. Filtering the last table obtain - First the raking row is created, ranking the day from higher to lower amount sold by each person and the filtering where this number is 1. 

```
SELECT *
FROM (
    SELECT 
        id,
        vendedor,
        region,
        monto,
        ROW_NUMBER() OVER (PARTITION BY vendedor ORDER BY monto DESC) AS rn
    FROM ventas
) t
WHERE rn = 1;
```
| id | vendedor | region | monto | rn |
| -- | -------- | ------ | ----- | -- |
| 2  | Ana      | Norte  | 200   | 1  |
| 4  | Luis     | Norte  | 300   | 1  |



### AGGREGATE FUNTIONS
Aggregate functions are used to perform calculations on a set of values (multiple rows) and return a single summary result. 
* COUNT(*) - Including NULL , COUNT (col) - just Not NULLS
* DISTINCT
* SUM()
* AVG() - Average
* MIN()
* MAX()
* STDEV() - Standar devistion
* VAR () - Variance
* GROUP_CONCATE -  Combines multiple string values into one with a separator.
* JSON_ARRAYAGG - To aggregate values into a JSON array.


###  WINDOW FUNCTIONS
SQL window functions (also known as analytic functions) perform calculations across a set of rows related to the current row without collapsing the results into a single output row. Unlike standard aggregate functions with GROUP BY, window functions retain the individual row details while providing the calculated insight.

* Aggregate : SUM(), AVG(), COUNT(), MIN(), MAX()
* RANKING - Assign rankings or row numbers within a group.
       - ROW_NUMBER(): Assigns a unique sequential number to every row (1, 2, 3, 4).
       - RANK(): Assigns the same rank to ties but skips subsequent numbers (1, 1, 3, 4).
       - DENSE_RANK(): Assigns the same rank to ties without skipping numbers (1, 1, 2, 3). 
       - NTILE(): 
* VALUE - Retrieve values from previous, next, or specific rows.
       - LEAD ()
       - LAG()
       - FIRST_VALUE ()
       - LAST_VALUE()

### JOINS 
The JOIN clause in SQL is used to combine rows from two or more tables based on a common column, allowing you to query related data and merge it into a single set of results. 
![JOIN TYPES](join_types.png)

```
SELECT table1.colY , table2.colX ...   FROM table1
INNER JOIN table2
ON table1.col = table2.col ;
```

Join Types:
* INNER - rows common to both tables in the specified column.
* LEFT JOIN / LEFT OUTER JOIN - ALL data from the first table and matching data from the second table; if there are missing values, they are filled with nulls.
* RIGHT JOIN / RIGHT OUTER JOIN - ALL data from the second table and matching data from the first table; if there are missing values, they are filled with nulls.
* FULL OUTER JOIN
* UNION

| Feature |FULL OUTER JOIN	|UNION|
|--------|-------|------|
|Data Growth|	Horizontal (adds columns)|	Vertical (adds rows)|
|Logic|	Joins rows based on a shared key (ON)	|Stacks results from separate queries|
|Null Values|	Creates NULLs for unmatched data	|Does not create NULLs based on keys|
|Requirements	|Requires a relationship between tables	|Requires identical column structures|


Notes:
*  In most database engines, JOINs work like INNER JOINs.
*  Same results can be achieved with RIGHT and LEFT JOINs by reversing the order of the tables, but in terms of data processing and compression, it is better to maintain a consistent order.
* For tables with N:M relationships, the query is performed by joining three tables (the two related tables and the intermediate table). 

```
SELECT table1.colX , table2.colY.... FROM table_relacion
INNER JOIN table1 ON table_relacion.col = table1.col
INNER JOIN  table2 ON table_relacion.col2 = table2.col2
```

### BOUNDERING
Boundering:
* UNBOUNDED PRECEDING 
* UNBOUNDED FOLLOWING
* N PRECEDING 
* N FOLLOWING
* CURRENT ROW 

### {CONDITIONS}
* LOGIC: 
     -  NOT, 
     - AND, 
     - OR,  
     - NOR  
* IN 
* BETWEEN
* MATH:
      -  >
      -  <  
      -  >= 
      -  <= 
* IS : 
      - IS ´string´
      - IS value
      - IS NOT value
      - NOT NULL
      - IS NULL 
* LIKE: - when exact value is unknown -
      - LIKE 
      - NOT LIKE 
            WHERE email LIKE '%@gmail.com'
            WHERE email LIKE 'sara%'
            WHERE email LIKE '%@%'

### BASIC SQL COMMANDS

#### SELECT
SELECT * FROM table_name; - Retrieve all data from a table
SELECT column_name FROM table_name;  - Retrieve a column from a table
SELECT column_name_1, column_name_2 FROM table_name;  - Retrieve multiple columns from a table

#### DISTINCT
SELECT DISTINCT * FROM users; - returns the unique records from the table, taking into account all columns

SELECT DISTINCT column_name FROM users; - returns the unique rows from the table, taking into account the specified column and its value

#### WHERE
The WHERE clause is used to filter records and retrieve only those that meet a specific condition. It is essential for limiting the results of a query to what you actually need.

SELECT * FROM table_name WHERE condition; 
SELECT column_name FROM table_name WHERE condition; 
SELECT DISTINCT column_name FROM table_name WHERE condition; 

#### ORDER BY 
The ORDER BY clause in SQL is used to sort the result set of a query in either ascending or descending order. By default, it sorts in ascending order.

SELECT * FROM users ORDER BY age;
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age DESC;

#### LIMIT 
The LIMIT clause in SQL is used to restrict the maximum number of rows returned in a result set. It is commonly used for performance optimization when working with large tables and for implementing features like pagination.

#### AS
In SQL, the AS keyword is primarily used to create aliases, which are temporary names for columns or tables that exist only for the duration of a query. 

#### GROUP BY
The SQL GROUP BY clause is used to organize rows with identical data into summary rows. It is most commonly used with aggregate functions (like COUNT, SUM, AVG) to perform calculations on each specific group. 

SELECT COUNT(age), age WHERE age > 16 FROM users GROUP BY age ASC;
SELECT COUNT(age), age FROM users GROUP BY age ASC;
SELECT MAX(age) FROM users GROUP BY age; 

#### HAVING
In SQL, the HAVING clause is used to filter results based on aggregate functions (like SUM, COUNT, AVG, MIN, or MAX).  **It was introduced because the standard WHERE clause cannot be used with aggregated data.**

SELECT age FROM users HAVING age > 6 
SELECT COUNT(age) FROM users HAVING COUNT(age) > 3 
SELECT COUNT(age) FROM user HAVING age > 6 -NO puede hacer esta operacion,seria con GROUP BY y WHERE  

#### CASE   
In SQL, the CASE expression is used to add conditional logic to your queries, similar to "if-then-else" statements in other programming languages. It evaluates a list of conditions and returns a value as soon as a condition is met.


SELECT *,
CASE
  WHEN age > 18 THEN 'Es mayor de edad'
  WHERE age = 18 THEN 'Acaba de cumplir la mayoría de edad'
  ELSE 'Es menor de edad'
END AS '¿Es mayor de edad?'
FROM users;



SELECT *,
CASE
  WHEN age > 17 THEN True
  ELSE False
END AS '¿Es mayor de edad?'
FROM users;

#### IFNULL 
The IFNULL(col, alt_value) function is primarily used to replace a NULL value with a default alternative.

SELECT name, surname IFNULL (age, 0) AS age FROM users;



## REFERENCES 

[SQL Documentation](https://w3schools.com/sql)
[SQL Course](https://www.youtube.com/watch?v=OuJerKzV5T0)
# FUNDAMENTAL CONCEPTS

[[_TOC_]]

## DATABASE (SQL) CONCEPTS

### RDBMS  
An RDBMS (Relational Database Management System) is a type of software application that allows users to create, manage, and manipulate relational databases, which store data in a structured, tabular format (rows and columns).

### DB Engine 
A Database Engine (or DB Motor/Storage Engine) is the underlying core component within a DBMS or RDBMS that specifically handles the task of actually writing, reading, updating, and deleting data on the physical disk or in memory.
RDBMS = DB Engine + administration + services + relational structure + user and permission management

### DB GUI
MySQL Workbench is a unified graphical user interface (GUI) tool for database architects, developers, and administrators to design, manage, and query MySQL databases.
SQL Server = the car's engine
Workbench = the dashboard and steering wheel for driving it


## TABLE RELATIONSHIPS

Table relationships are associations established between tables in a relational database, used to link data across tables based on common fields. They minimize data redundancy by separating data into subject-based tables, enabling complex queries by connecting related data through primary and foreign keys.

### RELATIONSHIP TYPES
![Table Relationships Types](table_relationships.png)
*  One-to-One (1:1): Each record in Table A corresponds to only one record in Table B. Often used for splitting data into smaller tables for security or efficiency.  Ex. One user has only one DNI.
* One-to-Many (1:N): The most common type. A single record in Table A can relate to multiple records in Table B. Example: One customer (1) places many orders (N).
* Many-to-Many (M:N): Records in both tables link to multiple records in each other, usually requiring a "junction" or "pivot" table to work. Example: Products can be in many orders, and orders can contain many products.
      -  An intermediary table, also known as a junction table, bridge table, or link table, is a specialized table used in relational databases to implement many-to-many  relationships. Because most databases cannot directly link two tables in a many-to-many fashion, an intermediary table breaks the relationship into two separate one-to-many relationships.
      ![Juntion table Example](junction_table.png)



* A self-referential (or recursive) table relationship occurs when a table has a foreign key that references its own primary key. This structure is used to model hierarchical data or relationships between entities of the same type within a single table, such as employees reporting to other employees.


### PK AND FK

* PRIMARY KEY - is a column or a set of columns that uniquely identifies each row in a table: 
* FOREIGN KEY - s a column (or collection of columns) that links two tables together by referencing the primary key of another table.
     |Feature| Primary Key (PK) | Foreign Key (FK) |
     | :--- | :---: | ---: |
     | Purpose | Uniquely identifies a record. | 	Links data between two tables. |
     | Uniqueness| Must be unique. | Can be duplicated. |
     |Nullability | Cannot be NULL.    |  Can be NULL.|
     | Quantity |  Only one per table.  | Multiple allowed per table.  |
     | Index |   	Automatically indexed.   |    Not always automatically indexed.   | 


## ADVANCES CONCEPTS

## INDEXES

An index in SQL is a special data structure—most commonly a B-tree—designed to speed up data retrieval from a table. It works like the index at the back of a textbook: instead of reading every page (a "full table scan") to find a topic, you look at the index to find the exact page number (a "pointer") and jump directly there. 

Common Types of Indexes
* Clustered Index: Determines the physical order of data in the table. Because data can only be sorted in one way, you can have only one clustered index per table (typically the Primary Key).
* Non-Clustered Index: A separate structure from the table data that contains a sorted list of values and pointers back to the original rows. You can have multiple non-clustered indexes on a single table.
* Unique Index: Ensures that all values in the indexed column(s) are distinct, preventing duplicate entries.
* Composite Index: An index created on two or more columns to speed up queries that filter by multiple criteria at once. 

The general syntax for creating an index follows this structure:
```
-- Standard Index
CREATE INDEX index_name 
ON table_name (column1, column2);

-- Composite Index
CREATE INDEX index_name 
ON table_name (column1, column2);


-- Unique Index
CREATE UNIQUE INDEX index_name 
ON table_name (column_name);

-- Removing an Index
DROP INDEX index_name;
```
Key Trade-offs
| Pros  |   	Cons|
| ------|------|
|Faster Searches: Significantly speeds up SELECT queries and WHERE filters.	|Slower Writes: Every INSERT, UPDATE, or DELETE requires updating the index, which adds overhead.|
|Efficient Joins: Speeds up the process of matching rows between multiple tables.	|Storage Space: Indexes are additional data structures that consume extra disk space.|
|Ordering: Improves the performance of ORDER BY and GROUP BY operations.	| Maintenance: Highly fragmented indexes may need periodic rebuilding for peak performance.|


## TRIGGER

A trigger in SQL is a special type of stored procedure that executes automatically in response to specific events on a table or view. Like a real-world trigger (e.g., pulling a gun trigger to fire a bullet), it initiates a predefined action when a specific "event" occurs in the database. 

Usage:
Triggers are typically used to automate backend tasks that would otherwise require manual intervention or complex application-side logic: 
* Data Validation: Checking that data meets specific rules before it is saved (e.g., ensuring a student's grade is between 0 and 100).
* Auditing: Automatically logging changes to a separate history table to track who modified data and when.
* Calculating Values: Updating a "total price" column whenever a new item is added to an order.
* Referential Integrity: Enforcing complex relationships between tables that standard foreign keys cannot handle. 

Types:
Database systems generally categorize triggers by the type of event that activates them: 
* DML Triggers: Fired by Data Manipulation Language events like INSERT, UPDATE, or DELETE.
* DDL Triggers: Fired by Data Definition Language events such as CREATE, ALTER, or DROP to monitor schema changes.
* Logon Triggers: Fired when a user session is being established (e.g., to control access or track login attempts). 

Trigger Timing
You can control exactly when the code runs relative to the event: 
* BEFORE: Runs before the data is modified. Ideal for validation or pre-calculating values.
* AFTER: Runs after the operation succeeds. Best for logging, auditing, or updating other related tables.
* INSTEAD OF: Runs in place of the standard action. Often used on views to direct writes to the correct underlying base tables. 

Basic Syntax:  
```
CREATE TRIGGER trigger_name
[BEFORE | AFTER] [INSERT | UPDATE | DELETE]
ON table_name
FOR EACH ROW
BEGIN
    -- Your SQL logic goes here
END;
```

Advantages & Disadvantages
|Pros |	Cons|
|----|-----|
|Automation: Reduces manual overhead for repetitive tasks.|	Performance Overhead: Can slow down bulk operations as they fire for every row.|
|Integrity: Enforces rules directly at the database level.	|Hidden Logic: Can cause unexpected side effects that are hard to debug.|
|Security: Can prevent unauthorized modifications to sensitive data.	| Complexity: Overuse makes the database structure harder to maintain.|

Example:

```
delimiter 

|

CREATE TRIGGER tg_email
AFTER UPDATE ON users
FOR EACH row
BEGIN 
 IF OLD.email <> NEW.email THEN 
     INSERT INTO email_history(user_id, email)
     VALUES user(OLD.user_id, OLD.email);
 END IF;
END;

|

delimiter;
```

Checking the created trigger:
```
UPDATE users SET email="bhabhaba@hkk.gmail.com"  WHERE user_id = 1;
```

Dropping a trigger
```
DROP TRIGGER tg_email;
```

## VIEW
In SQL, a view is a virtual table that is created from the results of a SELECT query. Unlike a regular table, a view does not store data physically; instead, it provides a dynamic "window" into the data stored in one or more underlying base tables. 

Key Functions
* Simplification: Encapsulates complex joins or calculations so you can query them as a single simple table.
* Security: Restricts user access to specific rows or columns without exposing the entire base table.
* Consistency: Ensures that the same business logic (like a specific calculation) is reused across different queries. 

```
--- Create: Use the SQL CREATE VIEW Statement to define a new view.

CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;

--- Query: Use it just like a regular table.
SELECT * FROM view_name;

--- Modify: Use CREATE OR REPLACE VIEW (in MySQL/Oracle) or ALTER VIEW (in SQL Server) to change its definition.

--- Remove: Use the DROP VIEW command to delete it. 
DROP VIEW view_name;
```

Common Types
* Simple View: Created from a single table; typically allows updates to the underlying data.
* Complex View: Created from multiple tables or contains functions/groups; these are generally read-only.
* Materialized View: Stores the actual result set physically to improve performance for heavy queries (called Indexed Views in SQL Server).


## STORED PROCEDURE

Are querys saved in "favorites". A stored procedure is a prepared collection of one or more SQL statements that are saved in a database so they can be reused repeatedly. Instead of writing the same query multiple times, you save it once as a named procedure and call it whenever needed. 

Key Benefits
* Improved Performance: Stored procedures are often precompiled, and SQL Server creates an execution plan for them, making subsequent runs much faster.
* Enhanced Security: You can grant users permission to execute a procedure without giving them direct access to the underlying tables.
* Reduced Network Traffic: Instead of sending hundreds of lines of SQL over the network, you only send a single EXEC command.
* Code Reusability: Logic is centralized in the database, allowing multiple applications to call the same consistent routine. 

Basic Syntax (SQL Server Example)

```
--- Create the Procedure
CREATE PROCEDURE SelectAllCustomers
AS
BEGIN
    SELECT * FROM Customers;
END;

--- Execute the Procedure 
EXEC SelectAllCustomers;
CALL SelectAllCustomers;

--- Modify
ALTER PROCEDURE proc_name;

--- Delete
DROP PROCEDURE proc_name;

--- View code
EXEC sp_helptext 'procedure_name';

```

Working with Parameters
Procedures can accept input parameters to filter results or output parameters to return specific values. 

```
--- Create procedure with parameter 
CREATE PROCEDURE GetCustomersByCity @City nvarchar(50)
AS
BEGIN
    SELECT * FROM Customers WHERE City = @City;
END;


--- Executing with a value:
EXEC GetCustomersByCity @City = 'London';

```
Stored Procedures vs. Functions
While both are reusable blocks of code, they serve different purposes: 

|Feature |	Stored Procedure|	Function|
|------|------|-----|
|DML Operations	|Can perform INSERT, UPDATE, DELETE	|Generally cannot modify data (read-only).|
|Usage	|Executed using EXEC or CALL	| Used inline within SELECT or WHERE|
|Return Value|	Can return multiple results or nothing	| Must return exactly one value or a table|



## TRANSACTIONS

An SQL transaction is a single logical unit of work that groups one or more database operations (like INSERT, UPDATE, or DELETE) to ensure they all succeed or fail together. This "all-or-nothing" approach prevents partial data updates, which can lead to corruption or inconsistencies. 

Transactions are managed using Transaction Control Language (TCL) commands: 
* BEGIN TRANSACTION: Marks the start of a transaction.
* COMMIT: Saves all changes made during the transaction permanently to the database.
* ROLLBACK: Undoes all changes if an error occurs, reverting the database to its state before the transaction began.
* SAVEPOINT: Creates a temporary marker within a transaction, allowing you to roll back only a specific portion of the work rather than the whole thing. 

The ACID Properties
To guarantee reliability, SQL transactions follow the ACID principle: 
* Atomicity: The entire transaction is treated as a single unit; if one part fails, the whole thing fails.
* Consistency: A transaction moves the database from one valid state to another, maintaining all rules and constraints.
* Isolation: Transactions running concurrently do not interfere with each other.
* Durability: Once a transaction is committed, its changes are permanent, even in the event of a system crash. 

Practical Example (Bank Transfer)
In a bank transfer, you must subtract money from one account and add it to another. If the system fails halfway, money could "disappear." A transaction prevents this: 

```
BEGIN TRANSACTION;

-- Deduct $100 from Account A
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';

-- Add $100 to Account B
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 'B';

-- Save changes only if both updates worked
COMMIT;
```

Types of Transactions
* Implicit: The database automatically starts and commits a transaction for every single DML statement (like a single INSERT).
* Explicit: The developer manually defines the boundaries using BEGIN and COMMIT/ROLLBACK.
* Distributed: Transactions that span across multiple databases or servers while maintaining consistency.

## CONCURRENCIA

Concurrency in SQL refers to the ability of a database to process multiple transactions simultaneously. To manage this without corrupting data, databases use concurrency control mechanisms that adhere to the ACID principle, specifically the "Isolation" property. 

Without proper control, overlapping transactions can cause several data anomalies: 
* Dirty Read: A transaction reads data that has been modified by another transaction but not yet committed. If the first transaction rolls back, the data becomes invalid.
* Lost Update: Two transactions update the same data simultaneously, and the final value overwrites one of the updates, losing that information.
* Non-repeatable Read: A transaction reads the same row twice but finds different data because another transaction modified and committed that row in between.
* Phantom Read: A transaction executes a query twice but receives a different set of rows (e.g., more rows) because another transaction inserted or deleted records. 

Concurrency Models
Databases typically follow one of two philosophies to handle these issues: 
* Pessimistic Model: Assumes conflicts will happen. It uses locks (shared for reading, exclusive for writing) to prevent others from accessing data while it is being used.
* Optimistic Model: Assumes conflicts are rare. It allows transactions to proceed without locking and checks for conflicts only at the time of commit (often using versioning or timestamps). 

SQL Isolation Levels
Developers use SQL isolation levels to balance performance and data consistency: 

|Isolation Level 	|Dirty Read	|Non-Repeatable Read|	Phantom Read|
|------|----|----|---|
|Read Uncommitted	|Possible	|Possible	|Possible|
|Read Committed	|Fixed	|Possible	|Possible|
|Repeatable Read	|Fixed	|Fixed	|Possible|
|Serializable|	Fixed	|Fixed	|Fixed|

Key Control Techniques
* Locking: Databases can lock data at various "granularities" (row, page, or entire table). Tools like SQL Server's Locking Architecture help manage these resources.
* Multi-Version Concurrency Control (MVCC): Used by PostgreSQL and Oracle, this allows readers to see a "snapshot" of data as it existed when their transaction started, so they aren't blocked by writers.
* Deadlock Handling: When two transactions wait indefinitely for each other's locks, the database engine automatically kills one (the "victim") to let the other proceed.
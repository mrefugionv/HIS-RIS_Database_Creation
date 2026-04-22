# SQL MODIFICATION COMMANDS
[[_TOC_]]

## RECORD LEVEL

Record-level SQL involves manipulating, locking, or securing individual rows rather than entire tables or databases.

### INSERT
INSERT INTO table_name ('colx_name', 'coly_name', ...) VALUES ('value_colx' 'value_coly'...)

´´´
INSERT INTO physicians (
physician_name,
date_of_birth,
speciality,
license_number,
contact_info,
room,
physician_status)
VALUES (
'MIRANDA VILLANUEVA ESPARZA',
'1978-12-04',
'General',
'DC-89-MX-2006',
'mirvillanueva@hosp.org.mx.com',
'Private_ERoom_5',
'active');
´´´
´´´

INSERT INTO patients (
first_name,
last_name,
date_of_birth,
gender,
contact_info,
primary_physician_id,
insurance_id,
patient_status)
VALUES (
'JUAN',
'CORONA VILLA',
'1967-08-16',
'Male',
'juancoronav@gmail.com',
2,
4678997,
'active');

SELECT * FROM patients;

´´´

```
INSERT INTO modalities (
modality_type,
ae_title,
ip_address,
modality_port,
location,
manufacturer
)
VALUES
('CT', 'CT_QRO_01', '192.168.1.50', 104, 'Sala 1', 'Siemens'),
('MG', 'MG_QRO_04', '192.168.1.49', 104, 'Sala 5', 'Cannon'),
('MR', 'MR_QRO_01', '192.168.1.51', 104, 'Sala 2', 'GE'),
('US', 'US_QRO_01', '192.168.1.52', 104, 'Sala 3', 'Philips');


```
A port is like a “logic gate” in a machine:
IP → identifies the device
Port → identifies the service on that device

Standard ports (by convention)
Service    Port
* HTTP    80
* HTTPS    443
* DICOM    104
Not mandatory, but standard

###  UPDATE 

ALWAYS USE A FILTER (WHERE)!
Otherwise, ALL the records in the field will be altered. 

Sometimes used for data type conversion:
* From string to int: Ex. age as a string.
* But the formats must be compatible: Ex. date and timestamp have their own specific formats. 

```
UPDATE users SET age = 21, init_date='2020-02-15'  WHERE user_id = 11;
```

### DELETE
ALWAYS USE A FILTER (WHERE)!
Otherwise, ALL the records in the field will be deleted. 

```
DELETE FROM users WHERE user_id = 11;
DELETE FROM physicians WHERE physician_id=1;
```

##  TABLE LEVEL
SQL table-level commands are used to create, modify, and manage the structure and data of tables.

### CREATE

```
CREATE TABLE `his_database`.`patients` (
  `patient_id` INT NOT NULL AUTO_INCREMENT,
  `medical_record_number` VARCHAR(15) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `gender` VARCHAR(15) NULL DEFAULT 'Not Specified',
  `contact_info` VARCHAR(45) NOT NULL,
  `primary_physician_id` INT NOT NULL,
  `insurance_id` INT ZEROFILL NULL,
  `status` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE INDEX `patient_id_UNIQUE` (`patient_id` ASC) VISIBLE,
  UNIQUE INDEX `medical_record_number_UNIQUE` (`medical_record_number` ASC) VISIBLE);
```

#### DATA TYPES
To decide what type of data to assign to each column, see
[SQL Data Type Documentation](https://www.w3schools.com/sql/sql_datatypes.asp)

#### CONSTRAINTS 
* NOTNULL - Cannot be null.
* UNIQUE - Unique value for each record.
* DEFAULT - Assign a value so that if the user does not enter anything in that field, it is not left blank but instead uses the default value.
* AUTO_INCREMENT - If no value is entered, the value immediately following the last entry in that field is assigned.
* CHECK - Evaluate a condition before saving.
* PRIMARY KEY - is a column or a set of columns that uniquely identifies each row in a table: 
* FOREIGN KEY - s a column (or collection of columns) that links two tables together by referencing the primary key of another table.
     |Feature| Primary Key (PK) | Foreign Key (FK) |
     | :--- | :---: | ---: |
     | Purpose | Uniquely identifies a record. | 	Links data between two tables. |
     | Uniqueness| Must be unique. | Can be duplicated. |
     |Nullability | Cannot be NULL.    |  Can be NULL.|
     | Quantity |  Only one per table.  | Multiple allowed per table.  |
     | Index |   	Automatically indexed.   |    Not always automatically indexed.   | 

###  DROP TABLE
```
DROP TABLE tabe_name;
```

### ALTER TABLE

Modify the table structure: add columns, rename columns, drop columns, change column data types, and add a constraint.

```
ALTER TABLE table_name
ADD col_name datatyp(len);  >>> añadir columna

ALTER TABLE table_name
RENAME COLUMN col_name TO new_col_name;   >> renombrar campo

ALTER TABLE table_name
MODIFY COLUMN col_name datatype(len); >> modificar tipo/longitud de dato

ALTER TABLE table_name
DROP COLUMN col_name;  >> Eliminar campo

ALTER TABLE table_name
ADD CONSTRAINT fk_col_name
FOREING KEY (col_name) REFRENCES table_2_name(col_name)
```

## TABLE RELATIONSHIPS

### 1:1  o 1:n

```
ALTER TABLE table_name
ADD CONSTRAINT fk_col_name
FOREING KEY (col_name) REFRENCES table_2_name(col_name)
```

### n:m

An intermediary table, also known as a junction table, bridge table, or link table, is a specialized table used in relational databases to implement many-to-many  relationships. Because most databases cannot directly link two tables in a many-to-many fashion, an intermediary table breaks the relationship into two separate one-to-many relationships.

**In this table, each record is a unique tuple of primary keys from other tables.**

![Juntion table Example](junction_table.png)

```
CREATE TABLE hero_team(
    hero_team_id int AUTO_INCREMENT PRIMARY KEY,
    hero_id int,
    team_id int,
    FOREING KEY (hero_id) REFRENCES hero(hero_id),
    FOREING KEY (team_id) REFRENCES team(team_id)
    UNIQUE (hero_id,team_id)
);
```

### SELF-REFERENCIAL

A self-referential (or recursive) table relationship occurs when a table has a foreign key that references its own primary key. This structure is used to model hierarchical data or relationships between entities of the same type within a single table, such as employees reporting to other employees.

 ```
 CREATE TABLE Employees (
    EmployeeID int NOT NULL PRIMARY KEY,
    Name varchar(255) NOT NULL,
    ManagerID int,
    -- Self-referencing foreign key constraint
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);
 ```

## DATABASE LEVEL

### CREATE DATABASE 
```
CREATE DATABASE database_name;
```

### DROP DATABASE
```
DROP DATABASE database_name;
```

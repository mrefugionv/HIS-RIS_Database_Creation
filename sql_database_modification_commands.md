# REGISTRY LEVEL
## INSERT
insertar registros

INSERT INTO table_name ('colx_name', 'coly_name', ...) VALUES ('value_colx' 'value_coly'...)

## UPDATE 
Actualizar registros
SIEMPRE PONER FILTRADO (WHERE) *** o todos los registros del campo se cambiaran 
Puede hacer algunas veces, la transformación de formato tipos de datos ej. edad de string , pero en date y timestamp tienen sus formatos específicos .


UPDATE users SET age = 21, init_date='2020-02-15'  WHERE user_id = 11;

## DELETE
SIEMPRE PONER FILTRADO (WHERE) *** o todos los registros se borran

DELETE FROM users WHERE user_id = 11;


# TABLE LEVEL

## CREATE
CREATE TABLE table_name (
  col_name_1 int NOTNULL AUTO_INCREMENT,
  col_name_2 varchar(20),
  col_name_3 datetime DEFAULT CURRENT_TIMESTAMP(),
  UNIQUE ('col_name'),
  PRIMARY KEY ('col_name'),
  CHECK (age => 18),
  FOREING KEY (col_name_table1) REFRENCES table_2_name(col_name_table2)
);

Data types > 
https://www.w3schools.com/sql/sql_datatypes.asp

Constraits o resticciones:
NOTNULL - no puede ser nulo
UNIQUE - Valor unico para cada registro
PRIMARY KEY- Clave primaria ayuda a crear relaciones con otras tablas.
FOREIGN KEY - 
CHECK - Antes de guardar evaluar alguna condicion
DEFAULT - Asignar algun valor para que si el usuario no registra nada en ese campo, no se quede nulo sino valor por defecto.
AUTO_INCREMENT - Si no se registra valor, se asigna el valor siguiente al ultimo dato en ese campo.

## DROP TABLE
DROP TABLE tabe_name;

## ALTER TABLE
Modificar ESTRUCTURA de la tabla

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

# TABLE RElATIONSHIPS

1:1  o 1:n

ALTER TABLE table_name
ADD CONSTRAINT fk_col_name
FOREING KEY (col_name) REFRENCES table_2_name(col_name)

n:m

CREATE TABLE users_languages(
    user_language_id int AUTO_INCREMENT PRIMARY KEY,
    user_id int,
    language_id int,
    FOREING KEY (user_id) REFRENCES users(user_id),
    FOREING KEY (language_id) REFRENCES languages(language_id)
    UNIQUE (user_id,language_id)
);

**tupla unica 
Autorefenrencial - no se hace explicita , ya esta en la misma tabla.

# DATABASE LEVEL

## CREATE DATABASE 
CREATE DATABASE database_name;

## DROP DATABASE
Eliminar base de datos
DROP DATABASE database_name;


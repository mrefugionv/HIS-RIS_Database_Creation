## 1. Descarga de SQLServer
  a)  MySQL Community (GPL) Downloads » MySQL Community Server - esto es la base de datos
  b) MySQL Installer Windows download” - mysql-installer-community-8.0.45.0.msi (556 MB)
  c) Configurar contraseña
  d) Crear y validar que tenemos nuestra base de datos corriendo en MySQL 8.0 Command Line Client:
       CREATE DATABASE his_database; 
       SHOW DATABASES;   -- lista que bases de datos tenemos
       USE his_database; -- Ahora todo lo que haga sera dentro de esta base de datos
       exit
![HIS_database creation in SQL Server by SQL Command Line ](sql_command_line.png)

## 2. Descarga de Database Management System DBMS , tambien llamado motor de base de datos. En este caso,  SQL Workbench.

## 3. Creación de nueva conneción
![Pantalla inicial de SQL Workbench y ventana que se abre al añadir conexión](db_creation.png)
   a) Dar nombre a conexión : HIS Simulation
   b) Hostname  es la IP , en este caso locla: 127.0.0.1
   c) Puerto 3306
   d) Username - root
   e) Dar nombre a Schema (Database): his_database

## 4. Creación de tablas
Segun el esquema propuesto en  [ ris-pacs-foundations/5_ris-pacs_integration.md] (https://github.com/mrefugionv/ris-pacs-foundations/blob/main/5_ris-pacs_integration.md)
[Descrito en](https://github.com/mrefugionv/ris-pacs-foundations/blob/main/5_ris-pacs_integration_ERdiagram.py)

Hay dos maneras de crear tablas:
a) A traves de la interfaz gráfica.
    Click derecho sobre "Tablas" en el Navegador de Schemas.
    Create Table
    En la ventana que se abre:
    a) Indicar nombre de la tabla
    b) Columnas - nombre, tipo de dato [SQL data types documentation] (https://www.w3schools.com/sql/sql_datatypes.asp)
    ,  y si es PK, NN, UQ, B, UN, ZF, AI, G ,  Características explicadas en 
    [sql_database_modification_commands.sql]()
    Default Expresión, valor por defecto en caso de que no se agregue valor.

    ![Creating "patients" table.](table_creation_window.png)

b) A traves de commandos. Explicados en  [sql_database_modification_commands.sql]()

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


### 5. Indicar constraints 
https://www.w3schools.com/sql/sql_check.asp

Operadores SQL:
=, <>, >, <
IN (...)
LIKE
REGEXP
BETWEEN
Funciones:
LENGTH()
LOWER()
UPPER()
https://www.w3schools.com/sql/sql_wildcards.asp

###  Checar formato
.ej. checar que contacto siempre tenga fomrato de email, en query , alterar tabla y agregar un constraint
[REGEXP Regular Expresion Documentation](https://www.geeksforgeeks.org/mysql/mysql-regular-expressions-regexp/)

```
ALTER TABLE patients
ADD CONSTRAINT chk_email
CHECK (contact_info REGEXP '^[^@]+@[^@]+\\.[^@]+$');

```
y checar que se haya guardado correctamente

```
SHOW CREATE TABLE patients;
```
![Adding email format constraint.](adding_constraint.png)

#### permitir solo ciertis valores - 
para mantener orden 
Tambien se puede cambiar nombre si se nota que alguno es palabra reseervada o restringida (Se pinta en azul)

```
ALTER TABLE patients
CHANGE status patient_status VARCHAR(15)
CHECK(patient_status IN ('active', 'inactive', 'deceased'));
```
#### SE guarde la fecha y hora del sistema

DATETIME	Guarda la fecha tal cual
TIMESTAMP	Se ajusta a zona horaria

👉 En sistemas reales:

TIMESTAMP → logs, auditoría
DATETIME → fechas clínicas (no quieres que cambien)

```
ALTER TABLE report 
MODIFY report_datetime DATETIME DEFAULT CURRENT_TIMESTAMP;
```


### 6. Creación de relaciones entre tablas - sql_database_modification_commands.sql
1:1 Study -report, 1 paciente 1 doctor de cabecera , 1 orden 1 estudio

```
ALTER TABLE  patients
ADD CONSTRAINT fk_patient_physician
FOREIGN KEY (primary_physician_id) REFERENCES physicians (physician_id);

ALTER TABLE  reports
ADD CONSTRAINT fk_report_study
FOREIGN KEY (study_id) REFERENCES studies(study_id);

ALTER TABLE  studies
ADD CONSTRAINT fk_study_request
FOREIGN KEY (request_id) REFERENCES order_requests(request_id);

```
ADD CONSTRAINT → estás agregando una regla
fk_patient_physician → nombre (puedes elegirlo- usualmente nombre de las tablas relacionadaS)
FOREIGN KEY (primary_physician_id) → columna local
REFERENCES physicians(physician_id) → a dónde apunta  tabla(columna)


1:n un physician - varios order request.
```
ALTER TABLE  order_requests
ADD CONSTRAINT fk_order_physician
FOREIGN KEY (ordering_physician_id) REFERENCES physicians(physician_id);
```


n:m  
ordering physician - ordenes -> studio, 
 technician - scheduled apointments -> studio

```
CREATE TABLE orders_physicians (
    request_id INT,
    physician_id INT,

    PRIMARY KEY (request_id, physician_id),

    FOREIGN KEY (request_id) REFERENCES order_requests(request_id),
    FOREIGN KEY (physician_id) REFERENCES physicians(physician_id)
);

CREATE TABLE appointments_technicians (
    appointment_id INT,
    performing_technician_id INT,

    PRIMARY KEY (appointment_id, performing_technician_id),

    FOREIGN KEY (appointment_id) REFERENCES scheduled_appointments(appointment_id),
    FOREIGN KEY (performing_technician_id) REFERENCES physicians(physician_id)
);

 ALTER TABLE studies
ADD CONSTRAINT fk_study_physician
FOREIGN KEY (ordering_physician_id) REFERENCES order_requests(ordering_physician_id);

ALTER TABLE studies
ADD CONSTRAINT fk_study_technician
FOREIGN KEY (performing_technician_id) REFERENCES scheduled_appointments(performing_technician_id);
```

AUTOREFRENCIAL
*crear base el MRN medical record nomber con una regla desde patiente id: ej EMD= HOSP(codigo hospital)-2026 (año)-paient_id



#### si se elimina alguna relación se elimina la info asociada?
ejemplo si se elimina un paciente se eliminan sus estudios? si se elimina algun estudio se elimina su reporte?

política de integridad de datos

Esto responde preguntas como:

¿qué se considera “dependiente”?
¿qué se puede borrar realmente?

CASCADE
SET NULL
RESTRICT / NOT ACTION

En este caso hare lo siguiente:
1. si elimino paciente , NO elimino sus estudios.

```
ALTER TABLE studies
DROP FOREIGN KEY fk_study_patient;

ALTER TABLE studies
ADD CONSTRAINT fk_studies_patient
FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
ON DELETE SET NULL;

```
2. si elimino un estudio, SÍ elimino su reporte.
```
ALTER TABLE reports
DROP FOREIGN KEY fk_report_study;

ALTER TABLE reports
ADD CONSTRAINT fk_report_study
FOREIGN KEY (study_id) REFERENCES studies(study_id)
ON DELETE CASCADE;
```

## 7. Triggers
a tabla log cada update/alter table

scheduled appointment - cuando se asigne hora , cambiar en tabla order request el status a scheduled. 
Cuando cambie en report a final, que cambie en order request status a completed 

Para las tablas criticas: paciente, estudio, reporte- queremos guardar cuando haya algun cambio en la tabla de audit_log. tiente los siguientes campos:
* log_id (ya esta predeterminado a autoincrement). 
* user_id -  @current_user_id
*action - si fue delete/update/insert 
*entityt type - el nombre de la tabla 
* entity_id - la clave primaria de la tabla que fue modificada 
*datetime - ya esta determinado el default current timestamp 
*previous value - 
*new value

En el campo de user se suele tomar del sistema, ahora lo vamos a setear cada ingreso de conexión: 
´´´
SET @current_user_id = 5;

UPDATE patients SET name = 'Maria R' WHERE patient_id = 1;
UPDATE patients SET email = 'nuevo@email.com' WHERE patient_id = 1;
´´´

´´´
SHOW CREATED TABLE nombretabla;
´´´
Ayuda a ver como esta codificada la tabla 


En l
1. Añadan se guarda el id 
        Pacientes - patient id
        Estudios - study _id
        Reportes - report_id 

´´´     
DELIMITER $$

CREATE TRIGGER trg_patients_insert
AFTER INSERT ON patients
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (
        user_id,
        log_action,
        entity_type,
        entity_id,
        new_value
    )
    VALUES (
        @current_user_id,
        'insert',
        'patients',
        NEW.patient_id,
        CONCAT('patient_id:', NEW.patient_id)
    );
END$$
´´´

2. cuando actualicen - id + solo el campo cambio actualizado, 
mediante comparaciones

´´´
DELIMITER $$

CREATE TRIGGER trg_patients_update
AFTER UPDATE ON patients
FOR EACH ROW
BEGIN

    -- Cambio en nombre
    IF NOT (OLD.first_name <=> NEW.first_name) 
       OR NOT (OLD.last_name <=> NEW.last_name) THEN

        INSERT INTO audit_log (
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
        )
        VALUES (
            @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT( 'name:', OLD.first_name, ' ', OLD.last_name),
            CONCAT('name:', NEW.first_name, ' ', NEW.last_name)
        );
    END IF;
    
    IF NOT (OLD.date_of_birth <=> NEW.date_of_birth) THEN
    INSERT INTO audit_log (
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
        )
    VALUES (
        @current_user_id,
        'update',
        'patient',
        NEW.patient_id,
        CONCAT('DOB:', OLD.date_of_birth),
        CONCAT('DOB:', NEW.date_of_birth)
        );
        END IF;
	
    IF NOT (OLD.gender <=> NEW.gernder) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT ('gender:',OLD.gender),
            CONCAT ('gender:', NEW.gender)
    );
    END IF;
    
    IF NOT (OLD.contact_info <=> NEW.contact_info) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT ('contact_info:',OLD.contact_info),
            CONCAT ('contact_info:', NEW.contact_info)
    );
    END IF;
    
    IF NOT (OLD.primary_physician_id <=> NEW.primary_physician_id) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT ('primary_physician_id:',OLD.primary_physician_id),
            CONCAT ('primary_physician_id:', NEW.primary_physician_id)
    );
    END IF;
    
	IF NOT (OLD.insurance_id <=> NEW.insurance_id) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT ('insurance_id:',OLD.insurance_id),
            CONCAT ('insurance_id:', NEW.insurance_id)
    );
    END IF;
    
    IF NOT (OLD.patient_status <=> NEW.patient_status) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'patient',
            NEW.patient_id,
            CONCAT ('insurance_id:',OLD.patient_status),
            CONCAT ('insurance_id:', NEW.patient_status)
    );
    END IF;

END$$

DELIMITER ;
´´´

#### STUDIES - algunos campos se bloquean para no modificarse

´´´
DELIMITER $$

CREATE TRIGGER trg_studies_update
AFTER UPDATE ON studies
FOR EACH ROW
BEGIN

    IF NOT (OLD.study_datetime <=> NEW.study_datetime) THEN
        INSERT INTO audit_log (
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
        )
        VALUES (
            @current_user_id,
            'update',
            'study',
            NEW.patient_id,
            CONCAT( 'study_datetime:', OLD.study_datetime),
        );
    END IF;
    
    IF NOT (OLD.modality_id <=> NEW.modality_id) THEN
    INSERT INTO audit_log (
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
        )
    VALUES (
        @current_user_id,
        'update',
        'study',
        NEW.patient_id,
        CONCAT('DOB:', OLD.modality_id),
        CONCAT('DOB:', NEW.modality_id)
        );
        END IF;
	
    IF NOT (OLD.body_part <=> NEW.body_part) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'study',
            NEW.patient_id,
            CONCAT ('body_part:',OLD.body_part),
            CONCAT ('body_part:', NEW.body_part)
    );
    END IF;
    
    IF NOT (OLD.study_status <=> NEW.study_status) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'study',
            NEW.patient_id,
            CONCAT ('study_status:',OLD.study_status),
            CONCAT ('study_status:', NEW.study_status)
    );
    END IF;
    
    IF NOT (OLD.performing_technician_id <=> NEW.performing_technician_id) THEN
    INSERT INTO audit_log(
            user_id,
            log_action,
            entity_type,
            entity_id,
            previous_value,
            new_value
            )
	VALUES (
	        @current_user_id,
            'update',
            'study',
            NEW.patient_id,
            CONCAT ('performing_technician_id:',OLD.performing_technician_id),
            CONCAT ('performing_technician_id:', NEW.performing_technician_id)
    );
    END IF;
    

END$$

DELIMITER ;
´´´ 
#### REPORTS
¿como se hace para logs de texto largo ?  
´´´ 

´´´ 

3. cuando eliminen - el id e info importante 
        Pacientes - patient id + first name + last name + fecha nacimiento (DOB)
        Estudios - study _id + patient_id + study datetime 
        Reportes - report_id + study_id + physician _id (radiologits)

´´´
DELIMITER $$

CREATE TRIGGER trg_patients_delete
AFTER DELETE ON patients
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (
        user_id,
        log_action,
        entity_type,
        entity_id,
        old_value
    )
    VALUES (
        @current_user_id,
        'delete',
        'patient',
        OLD.patient_id,
        CONCAT('name:', OLD.first_name, '', OLD.last_name, 'DOB', OLD.date_of_birth)
    );
END$$

´´´
## 7. Hacer conexión desde python - sql_connection.py

## 8. Crear y traer registros  - Se pueden usar los comandosde sql_query_commands.sql



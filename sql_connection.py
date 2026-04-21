# En este documento se hace una conexión a base de datos sql

import mysql.connector

config = {
    "host" :  "127.0.0.1",
    "port" : "3306",
    "database" : "his_database",
    "user" : "root",
    "password" : "Abuel1t4&YO!"
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()


def print_patient(patient):

    query = "SELECT * FROM patients WHERE first_name= %s;"
    cursor.execute(query, (patient,))
    result = cursor.fetchall()
    
    for row in result :
        print(row)
    
    cursor.close()
    connection.close()


print_patient("JUAN")
#print_user("DELETE TABLE users") --el codigo así no puede usarse si fuera "SELECT * FROM users" + users... --- tal vez se podría ehjecutar estas instrucciones peligrosas

"""
¡ BE AWARE !
Use the correct method for passing parameters; using text concatenation
can result in a dangerous SQL injection attack.

SQL injection (SQLi) is a critical web security vulnerability that 
allows attackers to interfere with database queries by inserting malicious 
SQL code into input fields. It enables unauthorized data access, modification, deletion,
or full system takeover. The attack exploits poor input validation, 
where user input is directly concatenated into SQL commands

References:
[SQL course](https://www.youtube.com/watch?v=OuJerKzV5T0)
6:00:00 

"""
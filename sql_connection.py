# En este documento se hace una conexión a base de datos sql

import mysql.connector

config = {
    "host" :  "127.0.0.1",
    "port" : "3306",
    "database" : "hello_mysql",
    "user" : "root",
    "password" : "Abuel1t4&YO!"
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

def print_user(user):
    query = "SELECT * FROM users WHERE name= %s;"
    cursor.execute(query, (user,))
    result = cursor.fetchall()
    
    for row in result :
        print(row)
    
    cursor.close()
    connection.close()


print_user("Brais")
#print_user("DELETE TABLE users")

'''
SQL injection - cuidado con la concatenación de texto 
cuando se quiere pasar parametro para la consulta por que 
puede terminar siendo una instrucción peligrosa de perdida de información.
Arriba la manera correcta de mandar parametros

https://www.youtube.com/watch?v=OuJerKzV5T0
6:00:00 
'''

# En este documento se hace una conexión a base de datos sql

import mysql.connector

config = {
    "host" :  "127.0.0.1",
    "port" : "3306",
    "database" : "Hello mySQL",
    "user" : "root",
    "password" : "Abuel1t4&YO!"
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

query = "SELECT * FROM users;"
cursor.execute(query)
result = cursor.fetchall()

for row in result :
    print(row)

cursor.close()
connection.close()

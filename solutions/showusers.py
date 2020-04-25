import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password ="",
                              database ="classicmodels")

mycursor = mydb.cursor()
mycursor.execute("select host, user from mysql.user")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import sys
import  mysql.connector

mydb = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="classicmodels")
cursor = mydb.cursor()

cursor.execute("select customerNumber, customerName, creditLimit from customers where customerName = '%s'" % (sys.argv[1]))


res = cursor.fetchall()

for x in res:
    print(x)
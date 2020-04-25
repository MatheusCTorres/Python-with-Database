import sys
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="classicmodels")

mycursor = mydb.cursor()

mycursor.execute("update customers SET customerNumber= " + sys.argv[1]+ 
                " , customerName= '%s'" % (sys.argv[2])+
                " , phone= " + sys.argv[3]+
                " , country= '%s'" % (sys.argv[4]) + " where customerNumber = 125")

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
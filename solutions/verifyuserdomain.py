import  mysql.connector

mydb = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="classicmodels")

mycursor=mydb.cursor()
mycursor.execute("select customers.customerName, Host from mysql.user, customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
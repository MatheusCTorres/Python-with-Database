import  mysql.connector

mydb = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="classicmodels")

mycursor=mydb.cursor()
mycursor.execute("select user, host from mysql.user where user = '{}' and host='{}'".format(sys.argv[1], sys.argv[2]))

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
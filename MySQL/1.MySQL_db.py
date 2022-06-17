import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Current-Root-Password",
    database="test"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE test")     #create DB
#mycursor.execute("DROP DATABASE test")       #delete whole DB
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
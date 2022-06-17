import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Current-Root-Password",
    database="test"
)

mycursor = mydb.cursor()

#Create/delete new table with primary key

#mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200), fav INT)")
#mycursor.execute("DROP TABLE customers")   #delete customers table

#Creating primary key on an existing table

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY)

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
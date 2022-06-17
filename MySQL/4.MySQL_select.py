import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Current-Root-Password",
    database="test"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM customers WHERE address ='Schevchenko 11'"
#mycursor.execute(sql)

mycursor.execute("SELECT * FROM products")                    #select all
#mycursor.execute("SELECT * FROM customers LIMIT 5")            #select the first 5 records from customers table
#mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")   #starts from 3rd position and returns 5 records
#mycursor.execute("SELECT * FROM customers ORDER BY name")      #select all ordered by name (ASC by default, DESC - descending order)
#mycursor.execute("SELECT name FROM customers")                 #selecting specific column

myresult = mycursor.fetchall()                   #returns all rows
#myresult = mycursor.fetchone()                  #returns first row

for x in myresult:
  print(x)
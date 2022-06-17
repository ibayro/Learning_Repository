import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Current-Root-Password",
    database="test"
)

mycursor = mydb.cursor()

#example = "INSERT INTO customers (name, address) VALUES (%s, %s)"   #%s prevents SQL Injection
#val = ("Ihor", "Liva 21")   #inserting a single row

users = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200), fav INT)"
u.values = [
  ('Ihor', 1),
  ('Alina', 2),
  ('Sabina', 3)
]

products = "CREATE TABLE products (id INT AUTO INCREMENT PRIMARY KEY, name VARCHAR(200)"
p.values = [
    (1, 'Music'),
    (2, 'Sport'),
    (3, 'Kats')
]

#sql1 = "DELETE FROM customers WHERE address = 'Schevchenko 11'"
#sql2 = "UPDATE customers SET address = 'Vasylkivska 9' WHERE address = 'Khreshatick 4'"

#mycursor.execute(sql1)         #deletes row with certain address
#mycursor.execute(sql2)         #overwrites the address column from Khreshatick 4 to Vasylkivska 9

#mycursor.execute(sql, val)     #insets a single row
#mycursor.execute(sql1)         #deletes row with certain address
mycursor.executemany(users, u.values)
mycursor.executemany(products, p.values)

mydb.commit()

print(mycursor.rowcount, "record inserted.")        #displays number of inserted rows
#print(mycursor.rowcount, "record(s) deleted")      #displays number of deleted rows
#print(mycursor.rowcount, "record(s) affected")     #displays overwritten row

name = input("Please, enter your name: ")

print("Hello" + ", " + name)

num1 = input("Enter X:")
num2 = input("Enter Y:")

summa = int(num1) + int(num2)

print(summa)

message = ""

while True:
    message = input("Enter Password")
    if message == "net":
        break
    print(message + "Password Not Valid")

print(message + " " + "Correct")

mylist = []
msg = ""

while msg != "stop":
    msg = input("Enter new item and stop to finish")
    mylist.append(msg)

print(mylist)
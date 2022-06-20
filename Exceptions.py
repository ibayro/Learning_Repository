import sys

filename = "sample.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='UTF-8')
    except Exception:
        print("Inside EXCEPT")
        print("Something went wrong, error occured")
        print(sys.exc_info())
        filename = input("Enter correct filename: ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()


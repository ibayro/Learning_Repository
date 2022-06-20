import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("You requested help")
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Argument not found")

os.system("dir > test.txt")
sys.exit()
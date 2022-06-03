from urllib import request
import sys

myURL = "http://adv400.tripod.com/kartinka.jpg"
myfile = "C:\\Users\\ASUS\\Downloads\\images\\adv.jpg"

try:
    print("Downloading file from: " + myURL)
    request.urlretrieve(myURL, myfile)
except Exception:
    print("Something went wrong")
    print(sys.exc_info())
    exit()

print("File downloaded and now stored at: " + myfile)
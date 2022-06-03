from urllib import request, parse
import sys

myURL = "https://www.google.com/search?"
value = {'q': 'Ukraine'}

my_header = {}
my_header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myURL = myURL + mydata
    req = request.Request(myURL, headers=my_header)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print("Error occurred during the search")
    print(sys.exc_info()[1])


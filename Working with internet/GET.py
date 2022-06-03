from urllib import request

myURL = "http://astahov.net"
answer = request.urlopen(myURL)
my_text1 = answer.readlines()
my_text2 = answer.read()


print(answer)
print(my_text2)

for line in my_text1:
    print(line)

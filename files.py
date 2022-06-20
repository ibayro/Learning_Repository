inputfile = "D:\python\sample3.txt"
outputfile = "D:\python\outputfile.txt"

word = "Quod"

myfile1 = open(inputfile, mode='r', encoding='UTF-8')
myfile2 = open(outputfile, mode='a', encoding='UTF-8')

for line in myfile1:
    if word in line:
        print("Found the word " + word + " outputfile.txt has been generated")
        myfile2.write("Found needed words:" + line)

myfile1.close()
myfile2. close()
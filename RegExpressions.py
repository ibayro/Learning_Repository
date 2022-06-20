import re

input_filename = "email_list.txt"
result_file = "results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
outputfile = open(result_file, mode='w', encoding='Latin-1')
mytext = inputfile.read()

"""
https://regex101.com/ - site to practice regular expressions

\d = any digit 0-9
\D = any non digit
\w = any alphabet symbol [A-Z a-z]
\W = sny non alphabet symbol
\s = breakspace
\S = non breakspace
(?!price\.info) excludes price.info

[0-9]{3} find three in a row digits
[A-Z][a-z]+ find words that start with capital letter with any other symbols
@\w+\.\w find domains
 
"""

lookfor = r"[\w.-]+@[A-Za-z-]+\.[\w.]+"
results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    outputfile.write(item + "\n")

print("Total: " + str(len(results)))
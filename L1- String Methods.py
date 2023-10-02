### Test variables ###
example = ("Test string for for for example")
x = example.center(50, "?")

""" Simple output """

print(example)

"""string.capitalize() 
Returns a string where the first character is upper case, and the rest is lower case.
"""

print(example.capitalize())

"""string.casefold()
Returns a string where all the characters are lower case.
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
"""

print(example.casefold())

"""string.center(length, character)
Center align the string, using a specified character (space is default) as the fill character.
length      Required. The length of the returned string
character   Optional. The character to fill the missing space on each side. Default is " " (space)
"""

print(x)

"""string.count(value, start, end)
Returns the number of times a specified value appears in the string.
value   Required. A String. The string to value to search for
start   Optional. An Integer. The position to start the search. Default is 0
end     Optional. An Integer. The position to end the search. Default is the end of the string
"""

print(example.count("for"))         #result is 3
print(example.count("for", 0, 20))  #result is 2


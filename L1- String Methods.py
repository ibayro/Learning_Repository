### Test variables ###
example = "Test string for for for example."
x = example.center(50, "?")
xx = example.endswith("for example.")
txt = "My name is Ståle"
tabs = "H\te\tl\tl\to"
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)


""" Simple output """

print(example)

"""
    string.capitalize() 
Returns a string where the first character is upper case, and the rest is lower case.
"""

print(example.capitalize())

"""
    string.casefold()
Returns a string where all the characters are lower case.
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
"""

print(example.casefold())

"""
    string.center(length, character)
Center align the string, using a specified character (space is default) as the fill character.
length      Required. The length of the returned string
character   Optional. The character to fill the missing space on each side. Default is " " (space)
"""

print(x)

"""
    string.count(value, start, end)
Returns the number of times a specified value appears in the string.
value       Required. A String. The string to value to search for
start       Optional. An Integer. The position to start the search. Default is 0
end         Optional. An Integer. The position to end the search. Default is the end of the string
"""

print(example.count("for"))         #result is 3
print(example.count("for", 0, 20))  #result is 2

"""
    string.encode(encoding=encoding, errors=errors)
Encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
encoding    Optional. A String specifying the encoding to use. Default is UTF-8
errors      Optional. A String specifying the error method. Legal values are:
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	        - ignores the characters that cannot be encoded
'namereplace'	    - replaces the character with a text explaining the character
'strict'	        - Default, raises an error on failure
'replace'	        - replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
"""

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="UTF-8",errors="xmlcharrefreplace"))

"""
    string.endswith(value, start, end)
Returns True if the string ends with the specified value, otherwise False.
value       Required. The value to check if the string ends with
start       Optional. An Integer specifying at which position to start the search
end         Optional. An Integer specifying at which position to end the search
"""

print(example.endswith("for example."))         #result is true
print(example.endswith("for example., 5, 11"))  #result is false

"""
    string.expandtabs(tabsize)
Sets the tab size to the specified number of whitespaces.
tabsize     Optional. A number specifying the tabsize. Default tabsize is 8
"""

print(tabs)
print(tabs.expandtabs())
print(tabs.expandtabs(2))
print(tabs.expandtabs(4))
print(tabs.expandtabs(10))


"""
    string.find(value, start, end)
Finds the first occurrence of the specified value.
value	    Required. The value to search for
start       Optional. Where to start the search. Default is 0
end         Optional. Where to end the search. Default is to the end of the string
"""

print(example.find("e"))            #result is 1 - "value is found"
print(example.find("e", 5, 10))     #result is -1 - "value is not found"

"""
    string.format(value1, value2...)
Formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}
"""

print(txt1)
print(txt2)
print(txt3)

"""
    string.index(value, start, end)
Finds the first occurrence of the specified value.
value       Required. The value to search for
start       Optional. Where to start the search. Default is 0
end         Optional. Where to end the search. Default is to the end of the string
"""

print(example.index("e"))           #result is 1 - first position
#print(example.index("python"))      #substring is not found

"""
    string.isalnum()
Returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9), otherwise False    
    string.isalpha()
Returns True if all characters in the string are in the alphabet (a-z), otherwise False
    string.isascii()
Returns True if all the characters are ascii characters  (a-z), otherwise False
    string.isdecimal()
Returns True if all the characters are decimals (0-9), otherwise False
    string.isdigit()
Returns True if all the characters are digits, otherwise False. Exponents, like ², are also considered to be a digit.
    string.isidentifier()
Returns True if the string is a valid identifier, otherwise False.
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
    string.islower()
Returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
    string.isnumeric()
Returns True if all the characters are numeric (0-9), otherwise False. Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
    string.isprintable()
Returns True if all the characters are printable, otherwise False. None printable character can be carriage return (\r) and line feed (\n).
    string.isspace()
Returns True if all the characters in a string are whitespaces, otherwise False.
    string.istitle()
Returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
Symbols and numbers are ignored.
    string.isupper()
Returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.
"""

print(txt1.isalnum())
print(txt1.isalpha())
print(txt1.isascii())
print(txt1.isdecimal())
print(txt1.isdigit())
print(txt1.isidentifier())
print(txt1.islower())
print(txt1.isnumeric())
print(txt1.isprintable())
print(txt1.isspace())
print(txt1.istitle())
print(txt1.isupper())
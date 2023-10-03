### Test variables ###
example = "Test string for for for example."
x = example.center(50, "?")
xx = example.endswith("for example.")
txt = "My name is Ståle"
tabs = "H\te\tl\tl\to"


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
value       Required. A String. The string to value to search for
start       Optional. An Integer. The position to start the search. Default is 0
end         Optional. An Integer. The position to end the search. Default is the end of the string
"""

print(example.count("for"))         #result is 3
print(example.count("for", 0, 20))  #result is 2

"""string.encode(encoding=encoding, errors=errors)
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

"""string.endswith(value, start, end)
Returns True if the string ends with the specified value, otherwise False.
value       Required. The value to check if the string ends with
start       Optional. An Integer specifying at which position to start the search
end         Optional. An Integer specifying at which position to end the search
"""

print(example.endswith("for example."))         #result is true
print(example.endswith("for example., 5, 11"))  #result is false

"""string.expandtabs(tabsize)
Sets the tab size to the specified number of whitespaces.
tabsize     Optional. A number specifying the tabsize. Default tabsize is 8
"""

print(tabs)
print(tabs.expandtabs())
print(tabs.expandtabs(2))
print(tabs.expandtabs(4))
print(tabs.expandtabs(10))


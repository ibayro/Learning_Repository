mystr = "test test string"
x = mystr.count("test")
x1 = mystr.center(20)
print(mystr.capitalize())	    #Returns a string where the first character is upper case, and the rest is lower case.
print(mystr.casefold())	        #Returns a string where all the characters are lower case. Stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
print(x1)	        #Center align the string, using a specified character (space is default) as the fill character.
print(x)	                    #Returns the number of times a specified value occurs in a string
print(mystr.encode())	        #Returns an encoded version of the string
print(mystr.endswith())	        #Returns true if the string ends with the specified value
print(mystr.expandtabs())	    #Sets the tab size of the string
print(mystr.find())	            #Searches the string for a specified value and returns the position of where it was found
print(mystr.format())        #Formats specified values in a string
print(mystr.format_map())	    #Formats specified values in a string
print(mystr.index())	        #Searches the string for a specified value and returns the position of where it was found
print(mystr.isalnum())	        #Returns True if all characters in the string are alphanumeric
print(mystr.isalpha())	        #Returns True if all characters in the string are in the alphabet
print(mystr.isascii())	        #Returns True if all characters in the string are ascii characters
print(mystr.isdecimal())	    #Returns True if all characters in the string are decimals
print(mystr.isdigit())	        #Returns True if all characters in the string are digits
print(mystr.isidentifier())	    #Returns True if the string is an identifier
print(mystr.islower())	        #Returns True if all characters in the string are lower case
print(mystr.isnumeric())	    #Returns True if all characters in the string are numeric
print(mystr.isprintable())	    #Returns True if all characters in the string are printable
print(mystr.isspace())	        #Returns True if all characters in the string are whitespaces
print(mystr.istitle())	        #Returns True if the string follows the rules of a title
print(mystr.isupper())	        #Returns True if all characters in the string are upper case
print(mystr.join())	            #Converts the elements of an iterable into a string
print(mystr.ljust())	        #Returns a left justified version of the string
print(mystr.lower())	        #Converts a string into lower case
print(mystr.lstrip())	        #Returns a left trim version of the string
print(mystr.maketrans())	    #Returns a translation table to be used in translations
print(mystr.partition())	    #Returns a tuple where the string is parted into three parts
print(mystr.replace())	        #Returns a string where a specified value is replaced with a specified value
print(mystr.rfind())	        #Searches the string for a specified value and returns the last position of where it was found
print(mystr.rindex())	        #Searches the string for a specified value and returns the last position of where it was found
print(mystr.rjust())	        #Returns a right justified version of the string
print(mystr.rpartition())	    #Returns a tuple where the string is parted into three parts
print(mystr.rsplit())	        #Splits the string at the specified separator, and returns a list
print(mystr.rstrip())	        #Returns a right trim version of the string
print(mystr.split())	        #Splits the string at the specified separator, and returns a list
print(mystr.splitlines())	    #Splits the string at line breaks and returns a list
print(mystr.startswith())	    #Returns true if the string starts with the specified value
print(mystr.strip())	        #Returns a trimmed version of the string
print(mystr.swapcase())	        #Swaps cases, lower case becomes upper case and vice versa
print(mystr.title())	        #Converts the first character of each word to upper case
print(mystr.translate())	    #Returns a translated string
print(mystr.upper())	        #Converts a string into upper case
print(mystr.zfill())	        #Fills the string with a specified number of 0 values at the beginning
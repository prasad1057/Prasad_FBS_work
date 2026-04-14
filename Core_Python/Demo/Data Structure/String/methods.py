
# //////Strings Methods///


'''

capitaliza()           -> Makes the first letter capital and the rest lowercase.
count()                -> Counts how many times a substring appears in a string.
endswith()             -> Checks if the string ends with a given value.
find()                 -> Returns the position (index) of the first occurrence of a substring. 
index()                -> Returns the index of a substring (gives error if not found).
isalnum()              -> Returns True if string contains only letters and numbers.
isalpha()              -> Returns True if string contains only alphabet letters.
isdigit()              -> Returns True if string contains only digits.
islower()              -> Returns True if all letters are lowercase.
isspace()              ->Returns True if string contains only spaces.
isuuper()              -> Returns True if all letters are uppercase.
join                   -> Joins elements of a list into one string using a separator.
lower()                -> Converts all letters to lowercase.
split()                -> Splits a string into a list using a separator.
replace()              -> Replaces a word or character with another.
startswith()           -> Checks if string starts with a given value.
strip()                -> Removes characters (or spaces) from both sides of a string.
swapcase()             -> Converts uppercase letters to lowercase and lowercase letters to uppercase.
title()                -> Converts the first letter of each word to uppercase.

'''


# Strings Are Immutable
a = "!!!!!Prasad!! !!!!! Prasad"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))     # rstrip is used to Skip that exlamentory mark but when you give exlametory in front of string it do not skip
print(a.replace("Prasad","Karan"))
print(a.split(" "))      # when space is present in string it separate that in two forms


heading = "introduaction tO python"
print(heading.capitalize())       # it used to get first letter capital and remaiing all letters make in small


str = "Welcome to the console"
print(len(str))
print(str.center(50))
print(len(str.center(50)))

# str1 = "My name is Prasad"
# print(len(str1))
# print(str1.center(50))
# print(len(str1.center(50)))

# str2 = "how are you??"
# print(len(str2))
# print(str2.center(45))
# print(len(str2.center(45))) 


str3 = "welcome to the Console!!!"
print(str3.endswith("!!!"))          # it check if end element are matching with those endswith function then give answer in true and false
print(str3.endswith("to",4 , 10))


str4 = "He's name is karan , he is an honnest man!"
print(str4.find("is"))       # it give first occrances of that element not another occurances 


str5 = "welcomeToTheConsole"
print(str5.isalnum())    # string only contain A-Z, a-z, 0-9 


str6 = "Welcome"
print(str6.isalpha())   # string only conatin A-z, a-z not numbers


str = "hello prasad hi"
print(str.islower())      # only conatin lower case


str = "wish you happy birthday bro\n"
print(str.isprintable())    # get only printable values (here \n it is not printable value it means it throws an errror)


str = "       "             # using sapcebar
print(str.isspace())
str = "             "         # using tab
print(str.isspace())


str = "Hello World"
print(str.istitle())           # it give true only if all starting word of letter are capital
str = "To kill a Mcking World"
print(str.istitle())


str = "Python is a Interprete language"
print(str.startswith("Python"))


str = "Python is a Interprete language"
print(str.swapcase())            # upper to lower and lower to upper


str = "His name is karan , he is an honnest man!"
print(str.title())             # make all starting letters of words are capital


# a = "!!!!Karan!!! !!! Karan"
# print(a)
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.split(" "))



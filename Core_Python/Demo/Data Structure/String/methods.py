
# //////Strings Methods///


'''
upper()         → Converts all characters in the string to uppercase.
lower()         → Converts all characters in the string to lowercase.
rstrip()        → Removes trailing spaces or characters from the right side of the string.
replace()       → Replaces a specified substring with another substring.
split()         → Splits the string into a list of words based on a separator (default is space).
center()        → Aligns the string in the center with specified width and fill character.
startswith()    → Returns True if the string starts with a specified value.
endswith()      → Returns True if the string ends with a specified value.
find()          → Returns the index position of the first occurrence of a substring.
isalnum()       → Returns True if the string contains only letters and numbers.
isalpha()       → Returns True if the string contains only alphabet letters.
islower()       → Returns True if all letters in the string are lowercase.
isprintable()   → Returns True if all characters in the string are printable.
isspace()       → Returns True if the string contains only whitespace characters.
istitle()       → Returns True if the string is in title case (each word starts with a capital letter).
swapcase()      → Converts uppercase to lowercase and lowercase to uppercase.
title()         → Converts the first letter of each word to uppercase.
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



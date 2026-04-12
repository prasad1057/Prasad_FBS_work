# /////Strings///////


name = "prasad"
apple = '''hi 
karan
how are you
i am fine
'''
sample = '''i am a good boy
whats about you
what are you doing

'''

print("Hello," +name)
print(apple)
print(name[0])    # p
print(name[1])     # locate that letter value     # r
print(name[2])      # a
print(name[3])       # s
print(name[4])        # a
print(name[5])          # d
# print(name[6])     # throws an error

print("Lets use a for loop\n")
for character in name :
    print(character)

for character in apple:
    print(character)

for character in sample:
     print(character)











#capitaliza()           -> Makes the first letter capital and the rest lowercase.

str1 = 'firstBit solution'      #first letter capital
res = str1.capitalize()
print(res)


#count()                -> Counts how many times a substring appears in a string.
s = "firstBit solution"
print(s.count("Bit"))       #1


#endswith()             -> Checks if the string ends with a given value.
s = "hello"
print(s.endswith("lo"))         #True


#find()                 -> Returns the position (index) of the first occurrence of a substring. 
s = "firstBit solution"
print(s.find("Bit"))        #5


#index()                -> Returns the index of a substring (gives error if not found).
s = "python"
print(s.index("th"))        #2


#isalnum()              -> Returns True if string contains only letters and numbers.
s = "abc123"
print(s.isalnum())          #True

#isalpha()              -> Returns True if string contains only alphabet letters.
s = "Python"
print(s.isalpha())          #True


#isdigit()              -> Returns True if string contains only digits.
s = "12345"
print(s.isdigit())          #True


#islower()              -> Returns True if all letters are lowercase.
s = "python"
print(s.islower())          #True


#isspace()              ->Returns True if string contains only spaces.
s = "   "
print(s.isspace())          #True


# Q. Calculate spaces in given string
str2 = 'FirstBit   Solutions'
count = 0
for i in str2:
    if i.isspace():
        count += 1

print(count)            #3


#isuuper()              -> Returns True if all letters are uppercase.
s = "HELLO"
print(s.isupper())          #True


#join                   -> Joins elements of a list into one string using a separator.
list1 = ['a','b','c']
res = '-'.join(list1)           #a-b-c
print(res)


#lower()                -> Converts all letters to lowercase.
s = "HELLO"
print(s.lower())            #hello


#split()                -> Splits a string into a list using a separator.
s = "hello world"
print(s.split(" "))         #['hello', 'world']


#replace()              -> Replaces a word or character with another.
str1 = 'FirstBit Solution'
res = str1.replace('Bit','Byte')            #firstByte solution
print(res)


#startswith()           -> Checks if string starts with a given value.
s = "python"
print(s.startswith("py"))           #True


#strip()                -> Removes characters (or spaces) from both sides of a string.
str3 = "['127.0.0.1']"
res = str3.strip("[]")              #'127.0.0.1'
print(res)


#swapcase()             -> Converts uppercase letters to lowercase and lowercase letters to uppercase.
s = "Hello World"
print(s.swapcase())         #hELLO wORLD



#title()                -> Converts the first letter of each word to uppercase.
s = "hello world from python"
print(s.title())                #Hello World From Python
# 3. Python Program to Detect if Two Strings are Anagrams

'''
Anagram = Same letters + Different order

Example 1

Listen → Silent

L I S T E N
S I L E N T
'''


str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")



str1 = str(input('Enter the string1: '))
str2 = str(input('Enter the string2: '))


str1 = str1.lower()
str2 = str2.lower()


if len(str1) != len(str2):
    print('String is not Anagram')
    
else:
    count = 0
    
    for i in str1:
        if i in str2:
            count += 1
            
    if count == len(str1):
        print('String is Anagram')
    else:
        print('String is not Anagram')
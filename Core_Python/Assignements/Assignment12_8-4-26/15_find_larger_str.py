# 15. Python Program to find larger string without using built-in functions.


def larger_string(str1,str2):

    len1 = 0 
    len2 = 0

    for i in str1:
        len1 += 1
        
    for j in str2:
        len2 += 1
        
    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are of equal length"
    
    

str1 = str(input('Enter the string: '))
str2 = str(input('Enter the string: '))

res = larger_string(str1,str2)

print("Larger string is:", res)
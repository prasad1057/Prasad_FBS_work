# 12. Python Program to count number of lowercase characters in a string.


def countLowercase(str1):
    
    count = 0
    
    for char in str1:
        if char.islower():
            count += 1
            
    return count

    
str1 = str(input('Enter the string: '))

res = countLowercase(str1)
print('Number is lowercase character is string:',res)
# 11. Python Program to replace every blank space with hyphen in a string.

def replaceBlank(str1):
    
    return str1.replace(' ','-')



str1 = str(input('Enter the string: '))
res = replaceBlank(str1)
print(res)
# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen


def replaceBlank():
    str1 = str(input('Enter the string: '))
    
    return str1.replace(' ','-')



res = replaceBlank()
print(res)
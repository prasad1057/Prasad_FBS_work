# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen


def replaceBlank(str1):
    
    return str1.replace(' ','-')



str1 = str(input('Enter the string: '))
res = replaceBlank(str1)
print(res)
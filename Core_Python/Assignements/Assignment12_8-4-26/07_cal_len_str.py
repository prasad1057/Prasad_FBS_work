# 7. Python Program to Calculate the Length of a String Without Using a Library Function


def countLenStr(str1):
    count = 0
    
    for i in str1:
        count += 1
        
    return count


str1 = str(input('Enter the string: '))

res = countLenStr(str1)
print('Length of String:',res)
# 8. Python Program to Remove the Characters of Odd Index Values in a String


def removeOddIdx(str1):
    
    result = ''
    
    for i in range(len(str1)):
        if i % 2 == 0:                  #store all even index values in result
            result += str1[i]
            
    return result
            

str1 = str(input('Enter the string: '))

res = removeOddIdx(str1)
print('After removing odd index values from string:',res)
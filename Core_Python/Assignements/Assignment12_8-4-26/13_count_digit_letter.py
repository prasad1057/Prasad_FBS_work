# 13. Python Program to count number of digits and letters in a string.


def countDigitLetter(str1):
    
    dig_count = 0
    let_count = 0
    
    for char in str1:
        if char.isdigit():
            dig_count += 1
        else:
            let_count += 1
            
    return dig_count,let_count


str1 = str(input('Enter the string: '))

d,l = countDigitLetter(str1)
print(f'Number is digit in string is {d} and letters are {l}') 
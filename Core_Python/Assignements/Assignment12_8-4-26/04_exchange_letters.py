# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged


def swap_first_last(str1):
    
    if len(str1) < 2:
        return str1
    
    # Exchange first and last characters
    new_string = str1[-1] + str1[1:-1] + str1[0]
    return new_string
    
    

str1 = str(input('Enter the string: '))

result = swap_first_last(str1)
print('After swapping first and last string :',result)
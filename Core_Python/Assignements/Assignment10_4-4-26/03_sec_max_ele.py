# 3. Write a program to find the second largest element in the list.


def SecMax(list1):
    
    max = list1[0]
    sec_max = 0
    
    count = 0
    for i in list1:         #to print the count of all elements present in the list
        count += 1
        
        
    for i in range(1,count):
        if list1[i] > max:
            sec_max = max
            max = list1[i]
            
        elif list1[i] > sec_max:
            sec_max = list1[i]
            
    return max,sec_max



list1 = [11,22,13,54,35,56,67,8,99,10]

max,sec_max = SecMax(list1)

print(f'Max ele is {max} and Sec Max ele is {sec_max}')
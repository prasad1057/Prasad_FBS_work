# 2. Write a program to find maximum and minimum element in a list.



def MinMax(list1):
    
    max = list1[0]
    min = list1[0]
    
    count = 0               #count = len(list1)   # Store the length in a variable
    
    for i in list1:         #to print the count of all elements present in the list         
        count += 1
    
    for i in range(1,count):
        if list1[i] > max:
            max = list1[i]
        
        if list1[i] < min:
            min = list1[i]  
            
    return max,min

list1 = [11,22,13,54,35,56,67,8,99,10]

max,min = MinMax(list1)

print(f'Max:{max}')
print(f'Min:{min}')
        


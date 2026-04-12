# 10. Write a program to print list after removing even numbers.



def removeEven(list1):
    
    new_list = []
    
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)
            
    return new_list

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

result = removeEven(list1)

print('After remvoing evene numbers:',result)
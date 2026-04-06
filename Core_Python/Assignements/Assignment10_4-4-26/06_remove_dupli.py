# 6. Write a program to remove duplicates from the list.


def remEle(list1,new_list):
    
    
    count = 0
    
    for i in list1:
        count += 1
        
    for i in range(0,count):
        
        if list1[i] not in new_list:
            new_list.append(list1[i])
            
    return new_list



list1 = [11,22,13,54,35,56,67,8,99,10,22,13,11]
new_list = []

print(remEle(list1,new_list))



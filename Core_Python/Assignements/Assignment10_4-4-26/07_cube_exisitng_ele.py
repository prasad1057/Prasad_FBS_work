# 7. Write a program to create a new list from existing list which contains cube of each number of list.

def cubeList(list1):
    
    # count = 0
    # for i in list1:
    #     count += 1
        
    # for i in range(1,count):
        
    #     cube_list.append(list1[i] ** 3)
    
    cube_list = []
    for i in list1:
        cube_list.append(i ** 3)
            
    return cube_list
    

list1 = [1,2,3,4,5,6,7,8,9,10]
print(cubeList(list1))



'''
def cubeList(list1, cube_list):
    
    for num in list1:
        cube_list.append(num ** 3)
            
    return cube_list
'''

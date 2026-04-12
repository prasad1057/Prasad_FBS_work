# 6. Python Program to Find the Union of two Lists
# UNION  --> Combine elements from both lists without repeating duplicates.

def unionNumber():
    
    union = []
    
    #Add elements from first list
    for i in list1:
        if i not in union:
            union.append(i)
            
    #Add elements from second list
    for j in list2:
        if j not in union:
            union.append(j)
            
    return union
    
    
    
list1 = (1,2,3,4,5,6,7)
list2 = (2,3,8,4,1,10)

result = unionNumber()
print(f'Union from two List: {result}')
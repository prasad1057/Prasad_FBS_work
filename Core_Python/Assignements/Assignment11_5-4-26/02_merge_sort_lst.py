# 2. Python Program to Merge Two Lists and Sort it



'''
list1 = [1, 4, 6, 3, 2]
list2 = [5, 8, 9, 12, 7]

list3 = list1 + list2
list3.sort()

print("After Merging two lists:", list3)
'''



# Using Bubble Sort
def bubbleMergeSort():
    
    list3 = list1 + list2
    #print(list3)
    
    size = len(list3)
    
    for i in range(1,size):
        
        for j in range(0, size - i):
            if list3[j] > list3[j+1]:
                list3[j], list3[j+1] = list3[j+1], list3[j]
                
    return list3



def selMergeSort():
    
    list3 = list1 + list2
    #print(list3)
    
    size = len(list3)
    
    for i in range(0,size - 1):
        ind = i
        
        for j in range(i+1, size):
            if list3[ind] > list3[j]:
                ind = j
                
        list3[i],list3[ind] = list3[ind],list3[i]
        
    return list3
    
    
    
    

list1 = [1,4,6,3,2]
list2 = [5,8,9,12,7]

print(f'List1:{list1}')
print(f'List2:{list2}')

a = bubbleMergeSort()
print('After Merging & Sorting two lists using bubble sort:',a)


b = selMergeSort()
print('After Merging & Sorting two lists using selection sort:',b)

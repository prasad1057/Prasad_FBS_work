def selectionSort():
    
    size = len(list1)
    
    for i in range(0,size - 1):
        ind = i
        
        for j in range(i+1, size):
            if list1[ind] > list1[j]:
                ind = j
                
        list1[i],list1[ind] = list1[ind],list1[i]
        
        
        
list1 = [60,30,10,50,40,20]

print('Before Swapping list:',list1)

selectionSort()

print('After Swapping list:',list1)
def bubbleSort():
    
    size = len(list1)
    
    for i in range(1, size):
        for j in range(0, size - i):
            
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
            
            
            
list1 = [60,50,40,30,20,10]
print('Before swapping list:',list1)

bubbleSort()
print('After swapping list:',list1)
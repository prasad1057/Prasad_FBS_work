# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort


def SecMax():
    
    size = len(list1)
    
    for i in range(1,size):
        for j in range(0,size - i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                
    # Second largest element
    return list1[size - 2]



list1 = [1,3,2,4,6,5,8,7,10,9]

a = SecMax()
print(f'Second Max Element of list: {a}')
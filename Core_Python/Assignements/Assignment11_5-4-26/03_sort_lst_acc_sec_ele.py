# 3. Python Program to Sort the List According to the Second Element in Sublist


'''
data = [
    [10, 3],
    [5, 8],
    [2, 1]
]

print(data[0][1])   # 2nd element of first sublist
print(data[1][1])   # 2nd element of second sublist
print(data[2][1])   # 2nd element of third sublist
'''



def bubbleSecEleSort():
    
    size = len(list1)
    
    for i in range(0, size):
        for j in range(0, size - i - 1):
            
            # Compare second element (index 1)
            if list1[j][1] > list1[j + 1][1]:
                
                # Swap entire sublists
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                

def SelecSecEleSort():
    
    size = len(list1)
    
    for i in range(0, size - 1):
        ind = i
        
        for j in range(i + 1, size):
            # Compare second element
            if list1[ind][1] > list1[j][1]:
                ind = j
        
        # Swap sublists
        list1[i], list1[ind] = list1[ind], list1[i]
                

list1 = [
    [10, 3],
    [5, 8],
    [2, 1],
    [7, 6]
]

bubbleSecEleSort()
print("After sorting according to second element using Bubble sort method:")
print(list1)

SelecSecEleSort()
print("After sorting according to second element using Selection sort method:")
print(list1)


'''
Note for loop:

###### bubbleSecEleSort() ###########


1️⃣ -1 is needed because we use j+1
If size = 4, the last index is 3.
list[j] and list[j+1]
So j must stop at size - 2.

2️⃣ - i is used because after each pass, the last elements are already sorted

In Bubble Sort:
1st pass → largest element goes to last position
2nd pass → second largest goes to second last
So we don't need to check them again
Therefore we reduce the loop each time.
'''

'''
5. Accept a number from user and check if this element is present in the list or
not. Also tell how many times it is present in the list.
'''



def addEle(list1):
    n = int(input('Enter the number of elements: '))

    for i in range(n):
        ele = int(input('Enter the element that u want to add in list: '))
        list1.append(ele)
        
    return list1
    


list1 = []

print(addEle(list1))

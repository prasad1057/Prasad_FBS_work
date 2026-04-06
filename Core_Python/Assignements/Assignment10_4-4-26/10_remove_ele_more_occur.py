# 10. Write a program to remove all occurrences of a given element in the list.


def remOccur(list1):
    
    ele = int(input('enter the number that u want to remove: '))
    
    while ele in list1:
        list1.remove(ele)
        
    return list1



list1 = [1,2,3,4,1,2,5,6,2,7,7,8,9,9,10]

result = remOccur(list1)

print('After removing occurances of given element:',result)


'''
9. Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements.
'''


def evenOdd(list1):
    
    n = int(input('Enter the elements: '))
    
    eve_lst = []
    odd_lst = []
    
    for i in range(n):
        ele = int(input('Enter the element that u want to add in list: '))
        list1.append(ele)
        
        if ele % 2 == 0:
            eve_lst.append(ele)
        else:
            odd_lst.append(ele)
            
    return eve_lst,odd_lst


list1 = []
even_list, odd_list = evenOdd(list1)


print('Original list:', list1)
print('Even elements:', even_list)
print('Odd elements:', odd_list)
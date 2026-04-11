# 1. Python Program to Put Even and Odd elements of a List into two Different Lists


def evenOdd():
    
    even_lst = []
    odd_lst = []
    
    for i in list1:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
            
    return even_lst,odd_lst
    
    
    
list1 = [1,2,3,4,5,6,7,8,9,10]

a,b = evenOdd()

print(f'Even List: {a} and Odd List: {b}')
# 1. Python Program to Put Even and Odd elements of a List into two Different Lists


def evenOdd(list1):
    
    even_lst = []
    odd_lst = []
    
    for i in list1:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
            
    return even_lst,odd_lst
    
    
    
list1 = []

n = int(input("Enter number of elements: "))

for i in range(n):
    ele = int(input("Enter number that you add in list: "))
    list1.append(ele)


a, b = evenOdd(list1)

print(f'Even List: {a}')
print(f'Odd List: {b}')
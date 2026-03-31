# Q. WAP to create list according to user
list5 = []

n = int(input('Enter the number of elements: '))

for i in range(n):
    element = int(input('Enter the element that u want to add in list: '))
    list5.append(element)               #list5 = list5 + [element]
    
print(list5)
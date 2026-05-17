# 13 . Write a program to print list after removing even numbers. 



def removeEven(list1):
    
    new_list = []
    
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)
            
    return new_list


list1 = []

n = int(input("Enter number of elements: "))

for i in range(n):
    ele = int(input("Enter number that you add in list: "))
    list1.append(ele)

print("Before removing even numbers:", list1)

result = removeEven(list1)

print("After removing even numbers:", result)
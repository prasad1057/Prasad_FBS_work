# 11. Write a program to print all numbers which are divisible by m and n in the list.

def devByMn(list1):
    
    m = int(input('enter the value of m: '))
    n = int(input('enter the value of n: '))
    
    print("Numbers divisible by", m, "and", n, "are:")
    
    for i in list1:
        if i % m == 0 and i % n == 0:
            print(i) 



list1 = [1,2,3,5,6,12,18,24,30,21,45,60]

devByMn(list1)
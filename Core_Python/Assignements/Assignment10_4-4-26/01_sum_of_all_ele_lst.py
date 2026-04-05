# 1. Write a program to find sum of all elements of list

list1 = [1,2,3,4,5,6,7,8,9,10]


sum = 0
count = 0

for i in list1:         #to print the count of all elements present in the list
    count += 1
    
#print(count)

for i in range(0,count):            #to sum all that elements
    sum += i
    
print(sum)
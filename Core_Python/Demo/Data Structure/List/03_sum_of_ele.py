import sys
list3 = [10,20,30,40,50]
print(sys.getsizeof(list3))     #104


print(len(list3))


# Q. WAP to calculate sum of all elements into the given list
list4 = [10,20,30,40,50]

sum = 0
for i in range(0,len(list4)):
    sum += list4[i]
    
print('Sum:',sum)






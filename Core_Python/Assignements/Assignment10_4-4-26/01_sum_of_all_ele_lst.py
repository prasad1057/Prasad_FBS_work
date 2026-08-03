# 1. Write a program to find sum of all elements of list

def listfun(num):
    
    list1 = []    
    for i in range(1,num+1):
        n = int(input('Enter the numbers that add into list: '))
        list1.append(n)
    
    return list1
    
    
num = int(input('ENter number: '))
result = listfun(num)
print('User Input List:',result)


def sumEle():
    
    sum = 0
    count = 0
    
    # for i in result:
    #     count += 1
    # print('COunt',count)
        
    # for i in range(0,count):
    #     sum += i
    
    for i in result:
        sum += i
    
    return sum

print(sumEle())
    




'''
list1 = [1,2,3,4,5,6,7,8,9,10]


sum = 0
count = 0

for i in list1:         #to print the count of all elements present in the list
    count += 1
                    #intead of using len() functio we use manually created count
#print(count)

for i in range(0,count):            #to sum all that elements
    sum += i
    
print(sum)

'''
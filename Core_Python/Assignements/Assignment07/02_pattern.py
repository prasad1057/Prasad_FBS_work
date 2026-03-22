'''
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''


n = int(input('Enter the number: '))

# UPper part
for i in range(1,n):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
#Lower part
for i in range(1,n):
    for j in range(1,n-i):
        print('*',end=' ')
    print()
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

#upper part
for i in range (1,n+1):
    
    for j in range(1,i+1):
        print('*',end=' ')
        
    print()
        
#lower part
for i in range(1,n+1):
    
    for k in range(1,n+1-i):
        print('*',end=' ')
        
    print()
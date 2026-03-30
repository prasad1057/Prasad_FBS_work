'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''


n = int(input('Enter the number: '))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
        
    for k in range(1,i+1):
        print('*',end=' ')
        
    for l in range(2,i+1):
        print('*',end=' ')
        
    print()
    
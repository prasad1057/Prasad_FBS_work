'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''


n = int(input('Enter the number: '))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
    for k in range(1,2*i):
        print('*',end=' ')

    print()
    
'''
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I 
'''



n = int(input('Enter the number: '))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
        
    for k in range(1,2*i):
        print(chr(64+k),end=' ')

    print()
    




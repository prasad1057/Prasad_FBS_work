'''
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
'''


n = int(input('Enter the number: '))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
        
    for k in range(1,2*i):
        print(k,end=' ')

    print()
    


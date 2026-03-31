'''
        1 
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''


n = int(input('Enter the number: '))

for i in range(1, n + 1):
    # 1. Leading spaces
    for j in range(1, n+1-i):
        print(' ', end=' ')
        
        
    # 2. Count up from i to (2*i - 1)
    for k in range(i, 2*i):
        print(k, end=' ')
        
        
    # 3. Count down from (2*i - 2) back to i
    for l in range(2*i-2, i-1,-1):
        print(l, end=' ')
        
    print()
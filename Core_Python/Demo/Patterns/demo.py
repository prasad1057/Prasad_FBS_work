for i in range(1,6):                    #  * * * *
    for j in range(1,6):                #  * * * *
        print('*', end=' ')             #  * * * *
    print()                             #  * * * *
    

print('-----------------------')


for i in range(1,6):                    #  1 1 1 1
    for j in range(1,6):                #  2 2 2 2
        print(i, end=' ')               #  3 3 3 3
    print()                             #  4 4 4 4
    
    
print('-----------------------')


for i in range(1,6):                    #  1 2 3 4 
    for j in range(1,6):                #  1 2 3 4 
        print(j, end=' ')               #  1 2 3 4 
    print()                             #  1 2 3 4 
   
   
   
print('-----------------------')


for i in range(1,6):                    #  * 
    for j in range(1,i+1):              #  * *
        print(j, end=' ')               #  * * *
    print()                             #  * * * *
     
     
print('-----------------------')


for i in range(1,6):                    # A
    for j in range(1,i+1):              # A B
        print(chr(64+j), end=' ')       # A B C
    print()                             # A B C D
    
    
print('-----------------------')


for i in range(1,6):                    # 4
    for j in range(5,5-i,-1):           # 4 3
        print(j, end=' ')               # 4 3 2
    print()                             # 4 3 2 1
    
    
print('-----------------------')


for i in range(1,6):                    # 4
    for j in range(1,i):                # 4 3
        print(j, end=' ')               # 4 3 2
    print()                             # 4 3 2 1
    
    
print('-----------------------')


for i in range(1,6):                    # * * * *
    for j in range(1,7-i):              # * * *
        print('*', end=' ')             # * * 
    print()                             # *
    

print('-----------------------')


for i in range(1,6):                    # 4 3 2 1
    for j in range(5,i-1,-1):           # 4 3 2
        print(j, end=' ')               # 4 3
    print()                             # 4
    
    
print('-----------------------')


for i in range(1,6):                    # 4 3 2 1
    for j in range(6-i,0,-1):           # 3 2 1
        print(j, end=' ')               # 2 1
    print()                             # 1
    
    
print('-----------------------')


for i in range(1,6):                    # A B C D
    for j in range(1,7-i):              # A B C 
        print(chr(64+j), end=' ')       # A B
    print()                             # A
    

print('-----------------------')

for i in range(1,6):                                          #   * * * * *
    for j in range(1,6):                                      #   *       *
        if (i == 1 or j == 1 or i == 5 or j == 5):            #   *       *
            print('*',end=' ')                                #   *       *
        else:                                                 #   * * * * *     
            print(' ', end=' ')
    print()


print('-----------------------')


for i in range(1,6):                                                         #   * * * * *
    for j in range(1,6):                                                     #   * *   * *
        if (i == 1 or j == 1 or i == 5 or j == 5 or i == j or i+j == 6):     #   *   *   *
            print('*',end=' ')                                               #   * *   * *
        else:                                                                #   * * * * *     
            print(' ', end=' ')
    print()
    

print('-----------------------')


for i in range(1,6):                                                         #   * * * * *
    for j in range(1,6):                                                     #   * *   * *
        if (i == 1 or j == 1 or i+j == 6):                                   #   *   *   *
            print('*',end=' ')                                               #   * *   * *
        else:                                                                #   * * * * *     
            print(' ', end=' ')
    print()
    
    

print('-----------------------')


for i in range(1,6):                    # 1 2 3 4
    for j in range(1,6-i):              # 1 2 3
        print(j, end=' ')               # 1 2
    print()                             # 1


print('-----------------------')


for i in range(1,6):                    # 1 
    for j in range(1,i+1):              # 1 2 
        print(j, end=' ')               # 1 2 3 
    print()                             # 1 2 3 4


print('-----------------------')


for i in range(1,6):                     
    for j in range(1,i+1):              
        print(j, end='')                
    if (i != 4):                        # 1+12+123+123412345+
        print('+',end='')
        
  
    
print('-----------------------')


for i in range(1,6):                           #  5 4 3 2 1
    for j in range(6-i,0,-1):                  #  4     1
        if (j == 1 or i == 1 or i + j == 6):   #  3   1
            print(j, end=' ')                  #  2 1
        else:                                  #  1
            print(' ',end=' ')
    print()                             
    
 
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
    for j in range(1,i):                #  * *
        print(j, end=' ')               #  * * *
    print()                             #  * * * *
     
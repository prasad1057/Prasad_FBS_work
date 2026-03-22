n = int(input('ENter the number: '))

for i in range(1,n+1):
    for j in range(i,n+1):
            if(j==i or j==n or i==1):      #i==1  ----- for print first row
                print(j,end=" ")
            else:
                 print(" ",end=" ")
    print()
    
    

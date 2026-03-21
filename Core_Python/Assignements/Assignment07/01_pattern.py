'''
     *
    * *
   *   *
  *     *
 *       *
  *     *
   *   *
    * *
     *
'''

n = int(input('Enter the number: '))

# upper part
for i in range(n):

    for j in range(n-i):
        print(" ", end="")

    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*", end="")
        else:
            print(" ", end="")

    print()


# lower part
for i in range(n-2,-1,-1):

    for j in range(n-i):
        print(" ", end="")

    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*", end="")
        else:
            print(" ", end="")

    print()


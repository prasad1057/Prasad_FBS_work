'''
        1   
      1   2
    1       3
  1           4
1   2   3   4   5
'''


n = int(input('Enter the number: '))

for i in range(1, n+1):

    # spaces for pyramid shape
    for j in range(n-i):
        print(" ", end=" ")

    for j in range(1, i+1):

        if j == 1 or j == i or i == n:
            print(j,' ', end=" ")
        else:
            print("  ",'', end=" ")

    print()
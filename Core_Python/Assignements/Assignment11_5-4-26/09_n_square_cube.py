# 9. Write a program to create three lists of numbers, their squares and cubes


def numSquareCube():
    
    numbers = []
    squares = []
    cubes = []
    
    n = int(input("Enter number of elements: "))
    
    for i in range(n):
        num = int(input("Enter number: "))
        
        numbers.append(num)
        squares.append(num ** 2)
        cubes.append(num ** 3)
        
    print("Numbers list:", numbers)
    print("Squares list:", squares)
    print("Cubes list:", cubes)


numSquareCube()
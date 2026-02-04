# 7.Program to Find the Roots of a Quadratic Equation

import math

def Find_Root(a,b,c):
    if a == 0:
        print('Not Possible')
        return
    
    discrement = b * b - 4 * a * c
    
    if discrement < 0:
        print('Not Possible')
        return
    
    sqrt_discrement = math.sqrt(discrement)
    
    root1 = math.floor((-b + sqrt_discrement) / (2.0 * a))
    root2 = math.floor((-b - sqrt_discrement) / (2.0 * a))
    
    if root1 < root2:
        root1,root2 = root2,root1
        
    print('Root1:', root1,'Root2:', root2)
    


# ---------- Main Program ----------
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

Find_Root(a,b,c)
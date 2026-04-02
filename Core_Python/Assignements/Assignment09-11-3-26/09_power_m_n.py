# 9. Write a program to calculate the m to the power n using recursion.


def power(m,n):
    if n == 0:
        return 1
    else:
        return m * power(m , n-1)


m = int(input("Enter base (m): "))

n = int(input("Enter power (n): "))

res = power(m,n)

print("Result is: ",res)
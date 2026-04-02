# 8. Write a program to check whether a number is prime or not using recursion.

# Recursive function to check prime
def prime_number(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return prime_number(n, i + 1)

num = int(input("Enter a number: "))

# Function call
if prime_number(num):
    print("Prime Number")
else:
    print("Not Prime Number")
# 10. Write a program to reverse a number using recursion.

def reverse_num(n,rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_num(n // 10 , rev)

num = int(input("Enter a number: "))

res = reverse_num(num)

print("Reversed number: ",res)
# 3. Write a program to reverse a given number using recursive function.

def reverse_no(n,rev=0):
    if n == 0:
        return rev
    
    digit = n % 10
    return reverse_no(n//10, rev * 10 + digit)

n = int(input('Enter number: '))


result = reverse_no(n)
print('Reverse Number:',result)
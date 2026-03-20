# Sum of Series

def sumofseries(n):
    if n > 0:
        return n + sumofseries(n - 1)
    elif n == 0:
        return 0
    else:
        return None

n = int(input('Enter the number: '))
res = sumofseries(n)
print('Sum of Series:',res)



# Factroial

def factroial(n):
    if n > 0:
        return n * factroial(n - 1)
    elif n == 0:
        return 1
    else:
        return None

n = int(input('Enter the number: '))
res = factroial(n)
print(f'Factroial of {n} is:',res)
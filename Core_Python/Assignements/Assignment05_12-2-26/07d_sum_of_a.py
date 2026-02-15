# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter the value a: "))

sum = 0

for i in range(1,11):
    term =  (a ** i)/i
    print(term)
    sum = sum + term

print("Sum of series: ",sum)
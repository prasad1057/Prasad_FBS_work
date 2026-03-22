# 4. WAP to print Armstrong number within a given range



n = int(input("Enter the range: "))

for num in range(1, n + 1):
    
    temp = num
    count = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10

    if num == sum:
        print(num, end=" ")
number = int(input('ENter the number: '))

temp = number

while(temp > 0):
    digi_sep = temp % 10        # last digit separate
    print(digi_sep)         # print last digit
    temp //= 10             #temp = temp // 10
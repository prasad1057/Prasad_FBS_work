number = int(input('Enter the number: '))
temp = number
rev_num = 0

while (temp > 0):
    digit = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + digit
    
    
if rev_num == number:
    print("Pallindrome")
else:
    print('Not a pallindrome')
    
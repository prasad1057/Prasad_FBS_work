# WAP to print all prime number between a range


num = int(input('Enter the number till prime number you want to print: '))

for num in range(2,num):
    for i in range(2,num):
        if (num % i) == 0:
            #print(f'{num} is not a prime number')
            break
        
    else:
        #print(f'{num} is a prime number')
        print(num)
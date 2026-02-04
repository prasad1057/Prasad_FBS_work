# 4. Write a program to enter P, T, R and calculate simple Interest.

principle   = int(input('Enter the principle: '))
rate        = float(input('Enter the rate of intrest: '))
time        = int(input('Enter the duration in years: '))

simple_intrest = (principle * rate * time) / 100

total_amount = principle + simple_intrest


print('THis is the simple intrest: ',simple_intrest)

print('Total amount is: ',total_amount)

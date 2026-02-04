# 5. Write a program to enter P, T, R and calculate Compound Interest.

principle = int(input('Enter the principle or original value(P): '))
rate = float(input('Enter the rate of intrest(R): '))
time = float(input('ENter time in years(T): '))

final_amount = int(principle * (1 + (rate * 0.01)) ** time)

compound_intrest = final_amount - principle

print('THe final amount is(A): ',final_amount)
print('Compound Interest is: ',compound_intrest) 


 
# 2. Write a program to calculate simple interest based on Principal,Rate and Time (SI = P*R*T/100)

priciple = int(input('Enter the Principle: '))
rate = int(input('Enter the rate: '))
time = float(input('ENter the time: '))

simple_intrest = (priciple * rate * time) / 100

print('Simple Interest is: ',simple_intrest)
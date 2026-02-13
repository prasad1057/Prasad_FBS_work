'''
3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.
'''

no_pass = int(input('Enter the number of passengers: '))
ticket_cost = int(input('Enter the ticket cost per passenger: '))

total_amount = 0

for i in range(1,no_pass+1):            # loop will run till number of passenger
    age = int(input(f'Enter the age of passenger {i}: '))           # we have to take age repreadtly so we write inside loop
    
    if age < 12:
        amount = ticket_cost * 0.70
    elif age > 59:
        amount = ticket_cost * 0.50
    else:
        amount = ticket_cost
    
    total_amount += amount          # add acutal price and discounted price in total amount
    
print(f"Total ticket amount for {no_pass} passengers: ",total_amount)
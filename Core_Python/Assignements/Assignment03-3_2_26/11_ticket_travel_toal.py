'''
11. Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.

Explanation: 
1. Ask age of 5 people
2. Ask ticket price per person
3. For each person:
4. Decide discount based on age
5. Calculate their payable ticket amount
6. Add all 5 payable amounts
7. Display total amount


Solution: 
Take ticket price
total_amount = 0
Repeat 5 times:
Input age
If age < 12 → 30% discount
Else if age > 59 → 50% discount
Else → full price
Add payable amount to total
Print total_amount
'''



'''

ticket_price = int(input('Enter the Ticket Price: '))

age1 = int(input('ENter the age1: '))
age2 = int(input('ENter the age2: '))

if age1 < 12:
    payable1 = ticket_price * 0.75

elif age1 < 59:
    payable1 = ticket_price * 0.50
    
else:
    payable1 = ticket_price
    

if age2 < 12:
    payable2 = ticket_price * 0.70

elif age2 < 59:
    payable2 = ticket_price * 0.50
    
else:
    payable2 = ticket_price
    
        
total_amount = payable1 + payable2
print(total_amount)

'''

ticket_price = int(input('ENter the Ticket Price: '))

total_amount = 0

for i in range(1,6):
    # name = input(f"Enter name of person {i}: ")
    # age = int(input(f"Enter age of {name}: "))
    
    age = int(input('Enter the age: '))
    
    if age < 12:
        payable = ticket_price * 0.70       # store the discounted price    # 30% discount
    elif age > 59:
        payable = ticket_price * 0.50       # 50% discount
    else:
        payable = ticket_price              # No discount
        
    #print(f"{name} has to pay: {payable}")
    total_amount = total_amount + payable       # store the actaul price after discounting
        
print("Total ticket amount for 5 people: ",total_amount)
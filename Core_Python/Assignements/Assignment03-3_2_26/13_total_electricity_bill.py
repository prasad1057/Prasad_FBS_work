'''
13. Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
'''

''''
🧠 Example (Simple)

If user consumes 200 units:
First 50 → 50 × 0.50
Next 100 → 100 × 0.75
Remaining 50 → 50 × 1.20

Then add all three.

First slab = 50 units
Remaining units = 120 - 50 = 70 units
'''



elec_unit_charge = int(input('ENter the Electricity Unit Charges: '))


if elec_unit_charge <= 50:
    total = elec_unit_charge * 0.50

elif 51 <= elec_unit_charge <= 150:
    total = (50 * 0.50) + (elec_unit_charge - 50) * 0.75
    
elif 151 <= elec_unit_charge <= 250:
    total = (50 * 0.50) + (100 * 0.75) + (elec_unit_charge - 150) * 1.20
    
else:
    total = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (elec_unit_charge - 250) * 1.50


total = total + (total * 0.2)

print(f'Total bill is {total}')
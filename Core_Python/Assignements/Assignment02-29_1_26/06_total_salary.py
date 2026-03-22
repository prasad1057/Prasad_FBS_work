# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

# da = Dearness Allowance
# ta = Travel Allowance
# hra = House Rent allowance

basic = float(input('Enter the basic value: '))

da = (basic * 10) / 100
ta = (basic * 12) / 100
hra = (basic * 15) / 100


# Calculate total salary
total_salary = basic + da + ta + hra

# Display total salary
print('Total salary of employee is:', total_salary)

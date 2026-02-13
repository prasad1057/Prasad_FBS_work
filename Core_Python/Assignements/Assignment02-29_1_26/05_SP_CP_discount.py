# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input('Enter the cost price: '))
discount = float(input('Enter the discount: '))

discount_amount = (cost_price * discount) / 100

seeling_price = cost_price - discount_amount

print('Selling price of the book is:', seeling_price)
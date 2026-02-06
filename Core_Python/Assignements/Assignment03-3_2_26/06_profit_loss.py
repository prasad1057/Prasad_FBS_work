# 6. Write a program to calculate profit or loss.

selling_price = int(input('ENter the Selling Price: '))
cost_price = int(input('ENter the Cost Price: '))

profit = selling_price - cost_price
loss = cost_price - selling_price

selling_price = int(input("Enter the Selling Price: "))
cost_price = int(input("Enter the Cost Price: "))



if selling_price == cost_price:
    print("No Profit and No Loss")

elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("Profit is:", profit)
    print("Profit Percentage is:", profit_percentage)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("Loss is:", loss)
    print("Loss Percentage is:", loss_percentage)

else:
    print("Something is wrong")

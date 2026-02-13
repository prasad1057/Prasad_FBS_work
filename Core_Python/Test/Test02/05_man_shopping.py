'''
5. A man goes for shopping. He buys 5 products. Accept the price of all products and 
display the total bill after adding 18% GST
'''

# GST=(Total×18)/100

product1 = int(input('Enter the prize of product1: '))
product2 = int(input('Enter the prize of product2: '))
product3 = int(input('Enter the prize of product3: '))
product4 = int(input('Enter the prize of product4: '))
product5 = int(input('Enter the prize of product5: '))

total_amount = product1 + product2 + product3 + product4+ product5
gst = (total_amount * 18) / 100
final_bill = total_amount + gst

print("\n----- BILL SUMMARY -----")
print("Total Amount:", final_bill)
print("GST (18%):", gst)
print("Final Bill Amount:", final_bill)

'''
choice = input("Do you want to generate the bill? (yes/no): ")

if choice.lower() == "yes":

    p1 = float(input("Enter price of product 1: "))
    p2 = float(input("Enter price of product 2: "))
    p3 = float(input("Enter price of product 3: "))
    p4 = float(input("Enter price of product 4: "))
    p5 = float(input("Enter price of product 5: "))

    total = p1 + p2 + p3 + p4 + p5
    gst = (total * 18) / 100
    final_bill = total + gst

    print("\n----- BILL SUMMARY -----")
    print("Total Amount:", total)
    print("GST (18%):", gst)
    print("Final Bill Amount:", final_bill)

else:
    print("Bill generation cancelled.")

'''
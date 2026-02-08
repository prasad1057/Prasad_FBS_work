'''
4. Calculate the cost of painting the following building’s walls 
(both interior and exterior). You need to accept area and cost of both 
interior and exterior wall. (Note: The figure shown consists of 
two adjacent rectangular shapes representing the building.)
'''


'''
🔹 Think in Real Life Terms
Painter says:

👉 “I charge ₹10 per square unit for inside walls”
👉 “I charge ₹15 per square unit for outside walls”

If you know the area, total cost = area × rate
'''


interior_area = float(input('Enter the area of interior wall: '))
interior_rate = float(input('Enter the rate of interior wall: '))

exterior_area = float(input('Enter the area of exterior wall: '))
exterior_rate = float(input('Enter the rate of exterior wall: '))

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate

total_cost = interior_cost + exterior_cost
print(f'Total cost of both wall is {total_cost}')





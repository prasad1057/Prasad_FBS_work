'''
3. A farmer has a field which is half in circle share and rest rectangle. He needs to do 
fencing for entire field using barbed wire 5 times. Circular section has radius 20m and
rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then 
calculate the total cost of fencing the field.
'''

'''
📐 Step 2: Given Data
Radius of half circle = 20 m
Rectangle length = 50 m
Rectangle breadth = 40 m
Wire fencing is done 5 times
Cost of wire = 35 Rs per meter

🧠 Step 1: Understand the Shape of the Field
📐 Step 2: Given Data
🟢 Step 3: Find Perimeter of Half Circle
🟦 Step 4: Perimeter of Rectangle
🟣 Step 5: Total Boundary (1 Round)
🔴 Step 6: Fencing Done 5 Times
💰 Step 7: Total Cost
'''

radius_half_circle = 20
length = 50
breadth = 40
cost_wire = 35
pi = 3.14

#Full circle circumference formula: 2 * π * r
#Half circle curved part: π * r
# Diameter: 2 * r
# Perimeterofhalfcircle= πr + 2r

perimeter_half_circle = (pi * radius_half_circle) + (2 * pi * radius_half_circle)
print(f'Perimter of half circle is {perimeter_half_circle} ')

perimter_rectangle = 2 * (length * breadth)
print(f'Perimter of rectangle is {perimter_rectangle}')


total_boundary = perimeter_half_circle + perimter_rectangle
print(f'Total boundary is {total_boundary}')

fencing = total_boundary * 5
print(f'Fencing is {fencing}')


total_cost = fencing * cost_wire
print(f'Total cost is {total_cost}')



'''
choice = input("Do you want to calculate total fencing cost? (yes/no): ")

if choice.lower() == "yes":
    
    radius = 20
    length = 50
    breadth = 40
    cost_per_meter = 35
    rounds = 5

    # Half circle perimeter
    half_circle = pi * radius + 2 * radius

    # Rectangle perimeter
    rectangle = 2 * (length + breadth)

    # Total boundary for one round
    total_boundary = half_circle + rectangle

    # Wire needed for 5 rounds
    total_wire = total_boundary * rounds

    # Final cost
    total_cost = total_wire * cost_per_meter

    print("Total Cost of Fencing:", round(total_cost, 2))

else:
    print("Calculation cancelled.")

'''
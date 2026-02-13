'''
4.Calculate the cost of painting the following building’s walls (both interior and exterior).
You need to accept area and cost of both interior and exterior wall.
'''

interior_cost = float(input('Enter the cost of interior wall: '))
interior_area = float(input('Enter the area of interior wall: '))

exterior_cost = float(input('Enter the cost of exterior wall: '))
exterior_area = float(input('Enter the area of exerior wall: '))


interior_total = interior_area * interior_cost
exterior_total = exterior_area * exterior_cost

cost_painting = interior_total + exterior_total

print(f'The total cost of painting is: {cost_painting}')
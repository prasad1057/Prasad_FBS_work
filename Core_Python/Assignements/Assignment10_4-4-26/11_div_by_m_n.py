# Write a program to print all numbers which are divisible by m and n in the list.

def devByMn(list1):

    m = int(input('Enter the value of m: '))
    n = int(input('Enter the value of n: '))

    divisible_list = []

    for i in list1:
        if i % m == 0 and i % n == 0:
            divisible_list.append(i)

    return divisible_list


list1 = []

size = int(input("Enter number of elements: "))

for i in range(size):
    ele = int(input("Enter number that you add in list: "))
    list1.append(ele)

result = devByMn(list1)

print("Original List:", list1)
print("Numbers divisible by both m and n:", result)

# list1 = [1,2,3,5,6,12,18,24,30,21,45,60]
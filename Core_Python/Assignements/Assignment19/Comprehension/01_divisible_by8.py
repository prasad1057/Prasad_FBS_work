# 1. Find all of the numbers from 1–1000 that are divisible by 8

# num1 = [ele for ele in range(1,81) if ele % 8 == 0]         # 8 ka table

num1 = [ele for ele in range(1,1001) if ele % 8 == 0]         # 8 ka table

print('Elements that are Divisible by 8 :')
print(num1)
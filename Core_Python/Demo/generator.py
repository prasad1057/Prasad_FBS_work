def genVal(n):
    for ele in range(1, n+1):
        yield ele
        
        
res = genVal(10)
print(res)

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))


for i in res:
    print(i)
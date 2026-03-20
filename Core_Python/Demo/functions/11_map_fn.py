# map() fucntion will return object

data = [10,20,30,40,50,60,70,80,90]

sq = lambda x : x ** 2
res = list(map(sq,data))
print(res)


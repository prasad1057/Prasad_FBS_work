
# /// List Methods ////

# list.append()
# list.reverse()
# list.sort()
# list.extend()
# print(list.count())
# print(list.index())


# ------------------


l = [12, 1, 2, 4, 5, 7, 5, 1, 1, 34]
print(l)
l.append(100)            #append means add that element in given list in last
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l.index(5))
print(l.count(5))           # to check how many times present that element in the list 


m = l.copy()
m = [800, 900, 1000]
# l.extend(m)                    # extend used to add this list in given(that) list
k = l + m
print(k)
print(l)



# papers = ["maths", "phy", "chem", "bee", "mechanics", "poc", "pcpf", "dbms"]
# print(papers)
# print(papers.count("maths"))
# papers.sort()
# papers.sort(reverse = True)
# print(papers.index("bee"))
# papers.reverse() 
# cars = ["scorpio", "bolero", "wagonar", "bmw", "tiago", "ertiga", "skoda"]
# k = papers + cars
# print(cars)
# papers.extend(cars)
# print(papers)



# f = ["mango", "apple", "banana", "guava", "chiku", "watermelon", "sitafal","chiku"]
# print(f)
# # f.append("ramfal")
# # f.reverse()
# # f.sort()
# # f.sort(reverse = True)
# # print(f.count("chiku"))
# # print(f.index("watermelon"))
# # print(f.index("chiku"))
# c = ["red","black", "blue", "yellow", "grey"]
# # f.extend(c)
# # k = f + c
# # print(k)
# print(f)


# city = ["panvel", "pune", "pen", "alibag", "khopoli", "delhi", "thane","banglore", "canada" ]
# print(city)
# # print(len(city))
# # city.append("thane")
# # city.reverse()
# # city.sort()
# # city.sort(reverse = True)
# print(city.count("thane"))
# print(city.index("alibag"))
# numbers = [1,2,4, 5]
# city.extend(numbers)
# k = city + numbers
# print(k)
# print(city)


# f2 = ["rose", "hibiscus", "zendu", "champa", "lotus"]
# print(f2)
# f2.append("flower")
# f2.reverse()
# f2.sort()
# f2.sort(reverse = True)
# print(f2.count("rose"))
# print(f2.index("zendu"))
# print(f2)

# //// Dictionary Methods ////


# update()
# clear()
# pop()
# popitem()               #lastone key value is eliminated
# del                     #delete all dictionary







d1 = {
    'id' : 101,
    'name' : 'Prasad',
    'age' : 22
}
print('d1:',d1)

#clear()
#d1.clear()



#cope()
d2 = d1.copy()
print('d2:',d2)


#get()
print(d1.get('name'))           #Prasad


#items()
print(d1.items())               #dict_items([('id', 101), ('name', 'Prasad'), ('age', 22)])


#keys()
print(d1.keys())                #dict_keys(['id', 'name', 'age'])


#keys()
print(d1.values())              #dict_values([101, 'Prasad', 22])


#pop()
# d1.pop('id')
# print(d1)                       #{'name': 'Prasad', 'age': 22}


#update
d1.update({'salary':1000, 'address':'Panvel'})
print(d1)                           #{'id': 101, 'name': 'Prasad', 'age': 22, 'salary': 1000, 'address': 'Panvel'}


#popitem()
print(d1.popitem())                 #('address', 'Panvel')
print(d1)                           #{'id': 101, 'name': 'Prasad', 'age': 22, 'salary': 1000}


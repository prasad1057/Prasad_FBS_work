# structure = {}
d1 = {
    1:'Python',
    2:'Java',
    3:'Testing'
}


# type of data : Hetergenous

d2 = {
    'id':101,
    'name':'Prasad',
    5:45000.55
}
print(d2)           #{'id': 101, 'name': 'Prasad', 5: 45000.55}
print(type(d2))     #<class 'dict'>



# changable : ele: mutable, val: mutable, key: immutable

# d2[6] : 3452
# d2[5] : 6766


# keys are unique, values can be duplicate

d3 = {
    1: 'Python',
    2: 'Java',
    2: 'Testing'
}

print(d3)       #{1: 'Python', 2: 'C'}          
# --> why it gives 2:C because alphbetically C comes first , if u give 2:Testing then it will give 2:Java as output beacuse alphabetically order.
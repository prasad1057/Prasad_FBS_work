x = 10
y = 20


# # MEthod 1 : DIrect Moduel import
# import my_module
# print(my_module.addition(x,y))



# # Method 2 : file name with module name
# from my_module import *
# print(addition(x,y))


# # Method 3 : Particular import
# from my_module import addition, subtraction
# print(addition(x,y))
# print(subtraction(x,y))


# Method 4 : alias name
from my_module import addition as add
print(add(x,y))
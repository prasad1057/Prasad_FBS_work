
##               DataTypes
'''
## categories 
   1. Numeric    ==  int
                   float
                   complex
   2. Boolean    ==  bool
   3. Text       ==  str
   4. Name Type
   5. Sequential == list[]
                    tuple()
                    range()
   6.set_type    == set{}
                    frozenset({})
   7.Mapping     == dict{}

'''

# 1.Numeric

x = 10
print(type(x))    # int
y = 3.14
print(type(x))    # float
z = 3 + 5j
print(type(z))          # complex

# 2.Text
a = "Hello"
b = 'joker'
c = '''Hii'''
print(type(a))    # str

# 3.Sequential
m = [10,20,30]
n = (1,2,3,'a')
o = range(1,10)
print(type(m))
print(type(n))
print(type(o))

# 4.setType

s = {1,2,3,'d'}
print(type(s))

s1 = frozenset({1,2,4,90})
print(type(s1))

# 5. Mapping
D = {1:'Python',
     2:'Java'}
print(type(D))

# 6. Boolean
B = True
print(type(B))

# 7. None Type
N = None
print(type(N))

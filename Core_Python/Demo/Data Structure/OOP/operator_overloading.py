class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        
    # def __str__(self):
    #     return f'{self.h}:{self.m}:{self.s}'
    
    def __add__(self, other):
        s = self.s + other.s
        m = s // 60
        s = s % 60
        
        m = self.m + other.m
        h = m // 60
        m = m % 60
        
        h = h + self.h + other.h
        return f'{h}:{m}:{s}'
    
    
t1 = Time(5,45,30)
t2 = Time(12,44,1)

print(t1 + t2)
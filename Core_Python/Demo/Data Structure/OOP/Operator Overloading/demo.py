class Number:

    def __init__(self, value):
        self.value = value

    # operator overloading
    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

result = n1 + n2

print(result.value)
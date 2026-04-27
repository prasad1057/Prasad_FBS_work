######  Static Variable

#1. Class Level Variable
#2. Use class name or object name to access the variable
#3. Single copy will created and shared to all objects


class BankAccount:
    branch = 'SBI Panvel'
    def __init__(self, acc_no, bal, holder_name):
        self.acc_no = acc_no
        self.bal = bal
        self.holder_nm = holder_name
        
    def display(self):
        data = f'ACC NO: {self.acc_no}\nBALANCE: {self.bal}\nHOLDER NAME: {self.holder_nm}\nBRANCH NAME: {BankAccount.branch}'
        return data
    

b1 = BankAccount(10001, 150, 'Prasad')
b2 = BankAccount(10002, 200, 'Karan')

res = b1.display()
print(res)

print('--------------')

res = b2.display()
print(res)

print('--------------')

print(BankAccount.branch)

print('-----------------------------------------')

class Student:
    clg = 'SCOE'
    def __init__(self, roll_no, name, dept_name):
        self.roll = roll_no
        self.name = name
        self.dname = dept_name
        
    def display(self):
        data = f'ROLL NO: {self.roll}\nNAME: {self.name}\nDEPT NAME: {self.dname}\nCOLLEGE NAME: {Student.clg}'
        return data
    
    
s1 = Student(1, 'Nikhil', 'IT')
s2 = Student(2, 'Pranav', 'Cyber')

res = s1.display()
print(res)
print('--------------')
res = s2. display()
print(res)
print('--------------')

print(Student.clg)




print('----------------Non-Static Variable-------------------------')


######  Non-Static Variable

#1. Object-Level / Instance-level Variable
#2. Use object name to access the variable
#3. Copies created according to the no. of objects

class BankAccount:
    def __init__(self, acc_no, bal, holder_name):
        self.acc_no = acc_no
        self.bal = bal
        self.holder_nm = holder_name
        
    def display(self):
        data = f'ACC NO: {self.acc_no}\nBALANCE: {self.bal}\nHOLDER NAME: {self.holder_nm}'
        return data
    

b1 = BankAccount(10001, 150, 'Prasad')
b2 = BankAccount(10002, 200, 'Karan')

print(b1.acc_no)        #--> here b2 object dont know the account number of b1 beacuse it is object lvel vvaribale , can access through that variable only 








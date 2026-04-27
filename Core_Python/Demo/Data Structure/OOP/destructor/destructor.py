class BankAccount:
    
    def __init__(self, acc_no, bal, holder_name):
        self.acc_no = acc_no
        self.bal = bal
        self.holder_nm = holder_name
        
    def display(self):
        data = f'ACC NO: {self.acc_no}\nBALANCE: {self.bal}\nHOLDER NAME: {self.holder_nm}'
        return data
    
    def __del__(self):
        print('This is Destrctor.....')
        
        
b1 = BankAccount(1001, 151, 'Prasad')
res = b1. display()
print(res)

'''
class BankAccount:
    
    def __init__(self, acc_no, bal, holder_name):
        self.acc_no = acc_no
        self.bal = bal
        self.holder_nm = holder_name
        
    def display(self):
        data = f'ACC NO: {self.acc_no}\nBALANCE: {self.bal}\nHOLDER NAME: {self.holder_nm}'
        return data
    
    def __del__(self):
        print('This is Destrctor.....')
        
        
b1 = BankAccount(1001, 151, 'Prasad')
del b1                                      --> bich me bhi hum us object ko destry kar sakte he
res = b1. display()
print(res)
'''

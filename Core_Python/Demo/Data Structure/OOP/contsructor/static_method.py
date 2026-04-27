class BankAccount:
    
    branch = 'SBI Panvel'
    
    def __init__(self, acc_no, bal, hol_name):
        self.acc_no = acc_no
        self. bal = bal
        self.hol_name = hol_name

    def display(self):
        data = f'ACC NO: {self.acc_no}\nBALANCE: {self.bal}\nHOLDER NAME: {self.holder_nm}\nBRANCH NAME: {BankAccount.branch}'
        return data
    
    @staticmethod               # decorator
    def displayBranch():
        return BankAccount.branch
    

b1 = BankAccount(10001, 150, 'Prasad')
    
#print(BankAccount.branch)      --> no need

print(BankAccount.displayBranch())

print(b1.displayBranch())

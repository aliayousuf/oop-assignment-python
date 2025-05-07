class Bank:
    bank_name = "MCB Bank" #class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()

print("Before change:")
print("b1 bank name:", b1.bank_name) 
print("b2 bank name:", b2.bank_name)  

Bank.change_bank_name("Faysal Bank")

print("\nAfter change:")
print("b1 bank name:", b1.bank_name)  
print("b2 bank name:", b2.bank_name) 
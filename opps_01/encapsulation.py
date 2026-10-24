#what is Encapsulation?
#Wrapping data and functions into a single unit(Object).

#Qcreate accunt classs with 2 attributes - balance & account
#create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was Debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total Balance: ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 5505)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
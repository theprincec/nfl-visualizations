class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount


bank_name=BankAccount('christian')

print(bank_name.__dict__)
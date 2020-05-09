class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance = (self.balance + amount)

    def make_withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('insufficient funds. choose a smaller amount')

    def check_balance(self, amount):
        self.balance = (self.balance - amount)
        if self.balance < 0:
            print('insufficient funds')
        else:
            print(self.balance)

    def is_balance_positive(self):
        if self.balance < 0:
            print('you do not have a positive balance')


# christian=BankAccount('christian')

# christian.make_deposit(800)
# print(christian.check_balance(1000))

# print(christian.__dict__)

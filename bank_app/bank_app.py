class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def check_balance(self, amount):
        if (self.balance - amount) >= 0:
            print('insufficient funds')

    def is_balance_positive(self):
        if self.balance < 0:
            print('you do not have a positive balance')


# class BankAccount(object):
#     def __init__(self, object):
#         self.name = object
#         self.balance = 0

#     def make_deposit(self, amount):
#         self.balance += amount

#     def make_withdrawl(self, amount):
#         self.balance -= amount

#     def check_balance(self, amount):
#         return (self.balance - amount) >= 0

#     def is_positive_balance(self):
#         return self.balance > 0

christian=BankAccount('christian')

christian.make_deposit(500)

print(christian.__dict__)
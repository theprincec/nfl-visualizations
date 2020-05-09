from helpers import BankAccount

name = input('Hi, What is your name?  ')

bank_account = BankAccount(name)

# initial_deposit = int(input(f"hi {name}, How much would you like to deposit?  $"))
# bank_account.make_deposit(initial_deposit)
# # print(bank_account.balance)

# print("select a number to make an action")
print('1. Deposit')
print('2. Withdrawal')
initial_decision = int(input("select a number to make an action:  "))
initial_option = ''
# while initial_decision is 1 or 2:
if initial_decision == 1:
    initial_deposit = int(input(f"hi {name}, How much would you like to deposit?  $"))
    bank_account.make_deposit(initial_deposit)
elif initial_decision == 2:
    initial_withdrawal = int(input(f"hi {name}, How much would you like to withdraw?  $"))
    bank_account.make_withdrawal(initial_withdrawal)
else:
    pass  

# print(f'your balance is:  ${bank_account.balance}')

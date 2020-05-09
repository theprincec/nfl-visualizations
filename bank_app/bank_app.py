from helpers import BankAccount

name = input('Hi, What is your name?  ')

bank_account = BankAccount(name)

# initial_deposit = int(input(f"hi {name}, How much would you like to deposit?  $"))
# bank_account.make_deposit(initial_deposit)
# # print(bank_account.balance)

print(f'Hi {name}, Thanks for banking! Here is your balance: ${bank_account.balance}')

# print("select a number to make an action")
print('1. Deposit')
print('2. Withdrawal')
initial_decision = int(input("select a number to make an action:  "))
# initial_option = ''
# while initial_decision is 1 or 2:
if initial_decision == 1:
    initial_deposit = int(input(f"hi {name}, How much would you like to deposit?  $"))
    bank_account.make_deposit(initial_deposit)
elif initial_decision == 2:
    initial_withdrawal = int(input(f"hi {name}, How much would you like to withdraw?  $"))
    bank_account.make_withdrawal(initial_withdrawal)
else:
    pass  

next_step = int(input(""""Would you like purchase one of the following items?
1. PNC hat ($40)
2. PNC Frisby ($10)
3. PNC t-shirt ($25)
4. make another deposit
"""))
# item_purchases = {1:{PNC}}
if next_step == 1:
    bank_account.make_withdrawal(40)
    print(f'your current balance is: $ {bank_account.balance}')
elif next_step == 2:
    bank_account.make_withdrawal(10)
    print(f'your current balance is: $ {bank_account.balance}')
elif next_step == 3:
    bank_account.make_withdrawal(25)
    print(f'your current balance is: $ {bank_account.balance}')
elif next_step == 4:
    new_deposit = int(input('How much do you want to deposit?'))
    bank_account.make_deposit(new_deposit)
    print(f'your new balance is:  ${bank_account.balance}')
else:
    pass



# print(f'your balance is:  ${bank_account.balance}')

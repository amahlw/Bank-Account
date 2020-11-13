import random


class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        account_number = random.randint(100001, 99999999)
        self.account_number = account_number
        self.balance = 0
        self.route_number = 98765432

    # function to set amount for deposit

    def deposit(self, amount):
        self.balance = self.balance + amount

    # withdraw

    def withdraw(self, amount):
        if self.balance-amount > 0:
            self.balance -= amount
            # return f"Your account balance is {account.print_balance(3456788)}"
        # balance decrease by amount withdrawn
        # self.balance = self.balance - amount
            # print(f"account balance is {withdraw}"

        else:
            self.balance -= 35
            print("Insufficient Funds")

    # interest

    def interest(self):
        rest = self.balance*0.00083
        self.balance = self.balance + rest

    # print balance

    def print_balance(self):
        return self.balance

    def print_receipt(self):
        print(self.full_name)
        # assisted by chegg tutor
        acc = str(self.account_number)
        print(acc)
        print('Account No.:****{}'.format(acc[4:]))
        print('Routing No.: {}'.format(self.route_number))
        print('Balance:${:,.2f}'.format(self.balance))

        # creating the instance


account1 = BankAccount('kash')

account1.deposit(100)
# account.deposit(100)
# account.deposit(400)
# account.print_balance()
# account.withdraw(700)
# account.print_balance()
# account.withdraw(1700)
# account.print_balance()

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
        # assisted by chegg tutor
        print("Amount Deposited: ${:,.2f}".format(amount))

#     # withdraw

    def withdraw(self, amount):
        if self.balance-amount > 0:
            self.balance -= amount
            # self.balance = self.balance - amount

        else:
            self.balance -= 35
            print("Insufficient Funds")

#     # interest

    def interest(self):
        rest = self.balance*.000089
        self.balance = self.balance - rest

#     # print balance

    def print_balance(self):
        # assisted by chegg tutor
        print("Your account  balance is ${:,.2f}".format(self.balance))

        return self.balance

        # print Reciept

    def print_receipt(self):
        print(self.full_name)
        # assisted by chegg tutor
        acc = str(self.account_number)

        print('Account No.:****{}'.format(acc[4:]))
        print('Routing No.: {}'.format(self.route_number))
        print('Your Account Balance is :${:,.2f}'.format(self.balance))

#         # creating the instance


# example 1
# account1 = BankAccount('Kash')
# account1.deposit(100)
# account1.print_receipt()


# example 2
# jo = BankAccount('Jovan')
# jo.deposit(1000)
# jo.deposit(20000)
# jo.print_receipt()
# jo.withdraw(500)
# jo.print_balance()


# example 3
eng = BankAccount('England Robert Wright')
eng.deposit(9000)
eng.withdraw(25)
eng.interest()
eng.print_receipt()

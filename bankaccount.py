

class BankAccount:
    def __init__(self, full_name, account_number, balance, route_number):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.route_number = route_number

    # function to set amount for deposit

    def deposit(self, amount):
        self.balance = self.balance + amount

    # withdraw
    def withdraw(self, amount):
        if self:
            self.balance -= amount
            return f"Your account balance is {account.print_balance(3456788)}"
        # balance decrease by amount withdrawn
        # self.balance = self.balance - amount
            # print(f"account balance is {withdraw}"

        else:
            print("Insufficient Funds")

    def print_balance(self, account_number):
        # return self.balance
        return f'You Balanace is {"print_balance"} Fro-Yo!'
        # print(self.balance)
        # print(self.account_number)

        # creating the instance


account = BankAccount("kash", 3456788, 0, 8900890)

account.deposit(100)
account.deposit(100)
account.deposit(400)
# return f"Your account balance is {account.print_balance(3456788)}"
account.print_balance(3456788)
account.withdraw(700)
account.print_balance(3456788)
account.withdraw(1700)
account.print_balance(3456788)

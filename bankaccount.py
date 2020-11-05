class BankAccount:
    def __init__(self, full_name, acct_number,):
        self.full_name = full_name
        self.acct_num = acct_num

    # function to set amount for deposit

    def deposit(self, amount):
        self.balance = self.balance + amount

    # withdraw
    def withdraw(self, amount):
        if self
        self.balance -= amount
        # balance decrease by amount withdrawn
        # self.balance = self.balance - amount
        else:
            print("Insufficient Funds")

    def print_balance(self):
        return self.balance

        # creating the instance


account = BankAccount()
account.deposit(100)
account.deposit(100)
account.deposit(400)
print(account.print_balance)

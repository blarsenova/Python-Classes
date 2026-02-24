class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.balance <= 0 or amount > self.balance:
            print(f"Hey {self.owner}, you do not have a sufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining: {self.balance}")

# 1. Create the account (The "Init" part)
my_account = BankAccount("Bob", 22)

# 2. Call the method on the account
my_account.withdraw(55)
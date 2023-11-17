class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than ₹0.00.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be greater than ₹0.00.")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount()

print(f"Initial balance: ₹{account.get_balance():.2f}")

account.deposit(1000)
account.withdraw(500)
account.deposit(2000)
account.withdraw(1500)

print(f"Final balance: ₹{account.get_balance():.2f}")

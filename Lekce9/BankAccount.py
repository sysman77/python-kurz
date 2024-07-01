"""
bankovní účty a typy účtů. Vytvoř základní třídu BankAccount s atributy balance
a metodami deposit() a withdraw(). Potom vytvoř podtřídu SavingsAccount,
které zdědí vlastnosti a metody z BankAccount a
mohou mít specifické operacepro daný typ účtu
"""


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.01):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest Added: {interest}, New Balance: {self.balance}")


# Příklady použití
# Vytvoření instance BankAccount
bank_account = BankAccount(100)
bank_account.deposit(50)
bank_account.withdraw(30)
print(f"Final Balance in BankAccount: {bank_account.get_balance()}")

# Vytvoření instance SavingsAccount
savings_account = SavingsAccount(200, 0.05)
savings_account.deposit(100)
savings_account.withdraw(50)
savings_account.add_interest()
print(f"Final Balance in SavingsAccount: {savings_account.get_balance()}")

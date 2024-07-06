
# creates the Class BankAcct
class BankAcct:
    def __init__(self, name, account_number, initial_amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate

    def withdraw(self, amount):
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        if days > 0:
            interest_amount = (self.amount * self.interest_rate * days) / 365
            return interest_amount
        else:
            return 0

    def __str__(self):
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate:.2f}%"


def test_bank_account():
    # Create an instance of BankAcct
    account1 = BankAcct("John Doe", "123456789", 1000.0, 5.0)

    # Print initial details
    print("Initial Details:")
    print(account1)
    print()

    # Test deposit and withdraw methods
    print("Testing deposit and withdraw:")
    account1.deposit(500)
    print(f"Balance after deposit: ${account1.get_balance():.2f}")
    account1.withdraw(200)
    print(f"Balance after withdrawal: ${account1.get_balance():.2f}")
    print()

    # Test adjust_interest_rate method
    print("Testing adjust_interest_rate:")
    account1.adjust_interest_rate(4.5)
    print(f"Interest rate adjusted to: {account1.interest_rate:.2f}%")
    print()

    # Test calculate_interest method
    print("Testing calculate_interest:")
    interest_amount = account1.calculate_interest(30)
    print(f"Interest amount for 30 days: ${interest_amount:.2f}")
    print()

    # Print final details
    print("Final Details:")
    print(account1)


# Run the test function
if __name__ == "__main__":
    test_bank_account()

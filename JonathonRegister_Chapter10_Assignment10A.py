class Money:
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add Money with different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract Money with different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor: float):
        return Money(self.amount * factor, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"


def test_money_operations():
    # Creating Money instances
    money1 = Money(100, "USD")
    money2 = Money(50, "USD")

    # Test addition
    sum_money = money1 + money2
    print("Addition:", sum_money)  # Expected: 150 USD

    # Test subtraction
    diff_money = money1 - money2
    print("Subtraction:", diff_money)  # Expected: 50 USD

    # Test multiplication
    product_money = money1 * 2
    print("Multiplication:", product_money)  # Expected: 200 USD

    # Test handling of different currencies
    try:
        money3 = Money(30, "EUR")
        money1 + money3  # This should raise an error
    except ValueError as e:
        print("Error:", e)  # Expected: Cannot add Money with different currencies


if __name__ == "__main__":
    test_money_operations()

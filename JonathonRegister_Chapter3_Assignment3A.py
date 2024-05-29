from functools import reduce


# creates the get_expenses function to get the user's inputs for types of expenses and amounts
def get_expenses():
    expenses = []
    # creates while loop to confirm the user is still inputting expenses
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        amount = float(input("Enter the amount for this expense: "))
        # adds the amount onto the expense type variable
        expenses.append((expense_type, amount))
    return expenses


# analyze_expenses function utilizes the reduce method to analyze the expenses
def analyze_expenses(expenses):
    # calculates the expenses added up, the grand total
    total_expense = reduce(lambda x, y: x + y[1], expenses, 0)
    # finds the highest expense from the user input
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    # finds the lowest expense from the user input
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)
    return total_expense, highest_expense, lowest_expense


# creates main function
def main():
    expenses = get_expenses()
    total_expense, highest_expense, lowest_expense = analyze_expenses(expenses)

    print("\nTotal Expense: $", total_expense)
    print("Highest Expense: $", highest_expense[1], "on", highest_expense[0])
    print("Lowest Expense: $", lowest_expense[1], "on", lowest_expense[0])


if __name__ == "__main__":
    main()

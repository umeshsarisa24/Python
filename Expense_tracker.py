expenses = []

def add_expense(amount, category):
    expenses.append({'amount': amount, 'category': category})

def view_expenses():
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def total_expenses():
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: {total}")

def main():
    while True:
        choice = input("Choose: [1] Add Expense, [2] View Expenses, [3] Total, [4] Exit: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

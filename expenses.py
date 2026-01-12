import json
from datetime import datetime

#class for each expense
class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

#expense tracker main class
class ExpenseTracker:
    def __init__(self, file_name="sampleData.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    #load expenses from file
    def load_expenses(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                return data.get("expenses", [])
        except FileNotFoundError:
            return []

    #save expenses to file
    def save_expenses(self):
        with open(self.file_name, "w") as f:
            json.dump({"expenses": self.expenses}, f, indent=4)

    #add expense
    def add_expense(self, expense):
        self.expenses.append(expense.to_dict())
        self.save_expenses()
        print("Expense added!")

    #show all expenses
    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nDate\t\t\tAmount\tCategory\tDescription")
        print("-" * 60)

        for e in self.expenses:
            print(
                f"{e['date']}\t${e['amount']:.2f}\t{e['category']}\t\t{e['description']}"
            )

    #total expenses
    def total_expenses(self):
        total = sum(e["amount"] for e in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

#simple CLI interface
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: $"))
            category = input("Category: ")
            description = input("Description (optional): ")
            tracker.add_expense(Expense(amount, category, description))

        elif choice == "2":
            tracker.show_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

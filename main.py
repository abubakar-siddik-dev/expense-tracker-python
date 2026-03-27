import json
from datetime import datetime

DATA_FILE = "data.json"

# Load data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data = load_data()
    data.append(expense)
    save_data(data)

    print("✅ Expense added!")

# View expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return

    for i, exp in enumerate(data, 1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")

# Total calculation
def total_expense():
    data = load_data()
    total = sum(exp["amount"] for exp in data)
    print(f"💰 Total Expense: {total}")

# Menu
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

# 📌 Student Expense Tracker (CLI)
# Uses: list, dictionary, set, functions, recursion

expenses = []   # list to store all expenses


def add_expense():
    amount = float(input("Enter amount spent: "))
    category = input("Enter category (food/travel/shopping/etc): ").lower()
    note = input("Optional note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("📌 No expenses recorded yet.\n")
        return

    print("\n📋 Expense List:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Amount: {exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")
    print()


# Recursion to calculate total spending
def total_spending(index=0):
    if index == len(expenses):
        return 0
    return expenses[index]["amount"] + total_spending(index + 1)


def category_analysis():
    if not expenses:
        print("📌 No data available for analysis.\n")
        return

    category_total = {}

    for exp in expenses:
        cat = exp["category"]
        category_total[cat] = category_total.get(cat, 0) + exp["amount"]

    print("\n📊 Spending by Category:")
    for cat, amt in category_total.items():
        print(f"{cat}: {amt}")

    highest = max(category_total, key=category_total.get)
    print(f"\n⚠ Highest spending category: {highest} ({category_total[highest]})\n")


def show_categories():
    categories = set(exp["category"] for exp in expenses)
    print("🗂️ Unique Categories:", categories, "\n")


def menu():
    while True:
        print("=== Student Expense Tracker 💰 ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Analysis")
        print("5. Show Categories")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total = total_spending()
            print(f"💵 Total Spending: {total}\n")
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            show_categories()
        elif choice == "6":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# Program starts here
menu()


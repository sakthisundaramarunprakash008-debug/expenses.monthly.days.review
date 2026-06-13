import csv
from collections import Counter
import matplotlib.pyplot as plt

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (Food, Travel, Shopping, Other): ")
    amount = float(input("Enter the amount spent: "))

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense saved successfully!\n")

def view_summary():
    categories = []
    amounts = []
    dates = []

    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            date, category, amount = row
            categories.append(category)
            amounts.append(float(amount))
            dates.append(date)

    print("\n--- Expense Summary ---")
    print("Total Expenses: ₹", sum(amounts))
    print("Category Totals:", Counter(categories))

    # Pie chart
    plt.pie(Counter(categories).values(), labels=Counter(categories).keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.show()

    # Bar chart
    plt.bar(dates, amounts)
    plt.xlabel("Date")
    plt.ylabel("Amount Spent (₹)")
    plt.title("Daily Expenses")
    plt.xticks(rotation=45)
    plt.show()

# Loop menu
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

import csv  # loads the CSV module

# Step 1: collect input
date = input("Enter the date (YYYY-MM-DD): ")
category = input("Enter the category (Food, Travel, etc.): ")
amount = float(input("Enter the amount spent: "))

# Step 2: save to CSV
with open("expenses.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date, category, amount])

print("Expense saved successfully!")

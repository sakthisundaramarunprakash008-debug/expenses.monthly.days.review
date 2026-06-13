import csv
import counter
categories = []
amounts = []
with open("Expenses.csv",mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
        date,amount,category = row
        print(f"date={date}, amount={amount}, category={category}")
        categories.append(category)
        amounts.append(float(amount))
print("\n--EXPENSES SUMMARY--")
print("total expenses:",sum(amounts))
print("categories totals:",counter(categories))
print("THE APPENDING PROGRAM IS CAME END")
        
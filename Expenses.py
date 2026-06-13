import csv
data=input("Enter a date(YY-MM-DD): ")
print("1.FOOD")
print("2.TRAVEL")
print("3.SHOPPING")
print("4.OTHERS")
choice=input("Enter number for category:")
categories = {
    "1":"FOOD",
    "2":"TRAVEL",
    "3":"SHOPS",
    "4":"OTHERS"
}
category=categories.get(choice,"others")
amount=float(input("Enter the amount spent: "))
with open('Expenses.csv', mode='a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([data, category, amount])
print("Expense recorded successfully!")
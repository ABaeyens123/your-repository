import csv
from datetime import datetime

def main_menu():
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    amount = input("Enter the amount: ")
    
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("Expense added successfully!")

def view_expenses():
    print("Expenses:")
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
    except FileNotFoundError:
        print("No expenses found. Add an expense first.")

def delete_expense():
    date = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    expenses = []
    
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = [row for row in reader if row[0] != date]

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print("Expense deleted successfully!")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


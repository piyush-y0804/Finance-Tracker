from datetime import date
import pandas as pd
import time

income = 0
expense = 0
TotalIncome = 0
TotalExpense = 0
Today = date.today()
global savings
savings = 0
global category

def FileWrite():
    with open("data.txt", "a") as f:
        f.write(f"{income}, {expense}, {category}, {Today}\n")

def CalculateMonthlyFinances():
    df = pd.read_csv(
        "data.txt",
        names=["Income", "Expense", "Category", "Date"]
    )
    
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    monthly_data = df.groupby("Month")[["Income", "Expense"]].sum()
    monthly_data["Savings"] = (monthly_data["Income"] - monthly_data["Expense"])
    monthly_report = monthly_data
    time.sleep(1)
    print(monthly_report)
    print("\n")
    time.sleep(1)


def CalculateFinances():
    global TotalIncome
    global TotalExpense
    with open("data.txt") as f:
        for y in f:
            z = y.split(", ")
            TotalIncome += int(z[0])
            TotalExpense += int(z[1])
            time.sleep(1)
    print("Your income is: ", TotalIncome)
    print("Your expense is: ", TotalExpense)
    savings = TotalIncome - TotalExpense
    print("Your saving is: ", savings, "\n")
    time.sleep(1)

def TakeInputIncome():
    return int(input("What is your income: \n"))

def TakeInputExpense():
    return int(input("What are the expenses(amount): \n"))

def TakeCategory():
    return input("Enter expense category (Food, Transport, Shopping, Bills, Entertainment, Other): ")

def TakeOption():
    return input("\nWhat would you like to do: \n " \
    "1.Add Income and Expense \n " \
    "2.See Financial Report \n " \
    "3. See Monthly Data \n " \
    "4. Exit \n " \
    "Please choose a number: ")

while True:
    option = TakeOption()
    print()
    if option == "1":
        income = TakeInputIncome()
        print("Income added successfully!")
        expense = TakeInputExpense()
        print("Expense added successfully!")
        category = TakeCategory()
        print("Category added successfully!")
        FileWrite()

    elif option == "2":
        CalculateFinances()

    elif option == "3":
        CalculateMonthlyFinances()

    elif option == "4":
        print("Successfully Logging Out \n")
        time.sleep(1)
        print("Thank You for using Finance Tracker! \n")
        break

    else:
        print("Please select a valid number! \n")
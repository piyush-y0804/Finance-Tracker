from datetime import date
import pandas as pd

income = 0
expense = 0
TotalIncome = 0
TotalExpense = 0
Today = date.today()
global savings
savings = 0

def FileWrite():
    with open("data.txt", "a") as f:
        f.write(f"{income}, {expense}, {Today}\n")

def CalculateMonthlyFinances():
    df = pd.read_csv(
        "data.txt",
        names=["Income", "Expense", "Date"]
    )
    
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    monthly_data = df.groupby("Month")[["Income", "Expense"]].sum()
    monthly_data["Savings"] = (
        monthly_data["Income"] - monthly_data["Expense"]
    )

    return monthly_data



def CalculateFinances():
    global TotalIncome
    global TotalExpense
    with open("data.txt") as f:
        for y in f:
            z = y.split(", ")
            TotalIncome += int(z[0])
            TotalExpense += int(z[1])

def TakeInputIncome():
    return int(input("What is your income: \n"))

def TakeInputExpense():
    return int(input("What are the expenses(amount): \n"))

def TakeOption():
    return input("\nWhat would you like to do: \n 1.Add Income and Expense \n 2.See Financial Report \n 3. See Monthly Data \n Please choose a number: ")

while True:
    option = TakeOption()
    print()
    if option == "1":
        income = TakeInputIncome()
        print("Income added successfully!")
        expense = TakeInputExpense()
        print("Expense added successfully!")
        FileWrite()

    elif option == "2":
        CalculateFinances()
        print("Your income is: ", TotalIncome)
        print("Your expense is: ", TotalExpense)
        savings = TotalIncome - TotalExpense
        print("Your saving is: ", savings, "\n")

    elif option == "3":
        monthly_report = CalculateMonthlyFinances()
        print(monthly_report)
    else:
        print("Please select a valid number! \n")
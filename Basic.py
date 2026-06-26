from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import time

income = 0
expense = 0
TotalIncome = 0
TotalExpense = 0
Today = date.today()
global savings
savings = 0
global category
category= ""
global categories

def FileWrite():
    with open("data.txt", "a") as f:
        f.write(f"{income}, {expense}, {category}, {Today}\n")


def ExpensePieChart():
    df = pd.read_csv(
        "data.txt",
        sep=",",
        names=["Income", "Expense", "Category", "Date"],
        skipinitialspace=True
    )

    category_expense = df.groupby("Category")["Expense"].sum()

    category_expense = category_expense[category_expense > 0]

    plt.figure(figsize=(8, 8))

    explode = [0.02] * len(category_expense)

    plt.pie(
        category_expense,
        labels=category_expense.index,
        autopct="%1.1f%%",
        startangle=90,
        explode=explode,
    )

    plt.title("Expense by Category")
    plt.axis("equal") 
    plt.show()


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
    print("Monthly Report \n")
    print("-" * 25)
    print(monthly_report)
    print("-" * 25)
    print("\n")
    time.sleep(1)


def CalculateFinances():
    global TotalIncome
    global TotalExpense
    TotalIncome = 0
    TotalExpense = 0

    with open("data.txt") as f:
        for line in f:
            income, expense, _, _ = line.strip().split(", ")
            TotalIncome += int(income)
            TotalExpense += int(expense)

    savings = TotalIncome - TotalExpense

    report = pd.DataFrame({
        "Amount": [TotalIncome, TotalExpense, savings]
    }, index=["Total Income", "Total Expense", "Savings"])

    print("\nFinancial Report")
    print("-" * 30)
    print(report)
    print("-" * 30)


def CategoryReport():
    df = pd.read_csv(
        "data.txt",
        sep=",",
        names=["Income", "Expense", "Category", "Date"],
        skipinitialspace=True
    )

    report = (
    df.groupby("Category")["Expense"]
      .sum()
      .reset_index(name="Total Expense")
    )

    print("\nExpense by Category\n")
    print("-" * 25)
    print(report)
    print("-" * 25)

    highest = report.loc[report["Total Expense"].idxmax()]
    print("\nHighest Spending Category")
    print("-" * 30)
    print(f"Category : {highest['Category']}")
    print(f"Amount   : ₹{highest['Total Expense']:,}")


def TakePositiveInteger(prompt):

    while True:

        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter a non-negative number.\n")
                continue

            return value

        except ValueError:
            print("Please enter a valid integer.\n")

def TakeInputIncome():
    return TakePositiveInteger("What is your income: ")

def TakeInputExpense():
    return TakePositiveInteger("What are the expenses(amount): ")


def TakeCategory():
    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Shopping",
        "4": "Bills",
        "5": "Entertainment",
        "6": "Healthcare",
        "7": "Other"
    }

    while True:

        for key, value in categories.items():
            print(f"{key}. {value}")

        choice = input("Choose a category: ")

        if choice in categories:
            return categories[choice]

        print("Invalid choice. Please try again.\n")


def TakeOption():
    while True:

        option = input(
            "\nWhat would you like to do:\n"
            "1. Add Income and Expense\n"
            "2. See Financial Report\n"
            "3. See Monthly Data\n"
            "4. See Expense by Category\n"
            "5. Exit\n"
            "Please choose a number: "
        )

        if option in ["1", "2", "3", "4", "5"]:
            return option

        print("Please choose a valid option.\n")

while True:
    option = TakeOption()
    print()
    if option == "1":
        income = TakeInputIncome()
        print("Income added successfully! \n")
        expense = TakeInputExpense()
        print("Expense added successfully! \n")
        category = TakeCategory()
        print("Category added successfully! \n")
        FileWrite()

    elif option == "2":
        CalculateFinances()

    elif option == "3":
        CalculateMonthlyFinances()

    elif option == "4":
        CategoryReport()
        print("\n")
        ExpensePieChart()

    elif option == "5":
        print("Successfully Logging Out \n")
        time.sleep(1)
        print("Thank You for using Finance Tracker! \n")
        break

    else:
        print("Please select a valid number! \n")
import os

income = 0
expense = 0
TotalIncome = 0
TotalExpense = 0

def FileWrite():
    with open("data.txt", "a") as f:
        f.write(f"{income}, {expense}\n")


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
    return input("\nWhat would you like to do: \n 1.Add Income and Expense \n 2.See Financial Report \n Please choose a number: ")

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
        print("your income is: ", TotalIncome)
        print("your expense is: ", TotalExpense, "\n")
    else:
        print("Please select a valid number! \n")
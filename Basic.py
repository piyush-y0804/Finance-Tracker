income = 0
expense = 0

def TakeInputIncome():
    return int(input("What is your income: \n"))

def TakeInputExpense():
    return int(input("What are the expenses(amount): \n"))

def TakeOption():
    return input("\n \nWhat would you like to do: \n 1.Add Income \n 2.Add Expense \n 3.See Financial Report \n Please choose a number: ")

while True:
    option = TakeOption()
    print()
    if option == "1":
        income = TakeInputIncome()
        print("Income added successfully!")
    elif option == "2":
        expense = TakeInputExpense()
        print("Expense added successfully!")
    elif option == "3":
        print("your income is: ", income)
        print("your expense is: ", expense, "\n")
    else:
        print("Please select a valid number! \n")
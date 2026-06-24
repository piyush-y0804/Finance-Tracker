income = 0
expense = 0

def TakeInputIncome():
    return int(input("What is your income: "))

def TakeInputExpense():
    return int(input("What are the expenses(amount): "))

income = TakeInputIncome()
expense = TakeInputExpense()
print("your income is: ", income)
print("your expense is: ", expense)
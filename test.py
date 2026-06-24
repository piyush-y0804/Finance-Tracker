TotalIncome = 0
TotalExpense = 0
def FinancialReport():
    with open("data.txt") as f:
        for y in f:
            z = y.split(", ")
            TotalIncome += int(z[0])
            TotalExpense += int(z[1])
        print(TotalIncome)
        print(TotalExpense)
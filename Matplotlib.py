# Kevin Gemian
# Expense Pie Chart
# CS 175
import matplotlib.pyplot as plt

def createPieChart(expenseAmounts, expenseNames):
    plt.pie(expenseAmounts, labels=expenseNames)
    plt.title("Monthly Expenses")
    plt.show()

def main():
    expenseNames = []
    expenseAmounts = []
    with open("expenses.txt", "r") as file:
        count = 0
        for line in file:
            stuff = line.strip().split("\t")
            num = stuff[0]
            if len(stuff) == 2:
                try:
                    expenseNames.append(num)
                    amount = float(stuff[1])
                    expenseAmounts.append(amount)
                except ValueError:
                    print(f"INVALID NUMBER: {num.upper()}")
                    expenseNames.pop(count)
            count += 1
    createPieChart(expenseAmounts, expenseNames)


if __name__ == "__main__":
    main()
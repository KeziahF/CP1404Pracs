"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of num_months."""
    incomes = []
    num_months = int(input("How many num_months? "))

    for month in range(1, num_months + 1):
        income = float(input("Enter income for month %s : " %(month)))
        incomes.append(income)

    print_Report(incomes, num_months)


def print_Report(incomes, num_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f}   Total: ${:10.2f}".format(month, income, total))


main()
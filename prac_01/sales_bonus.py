"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MENU = """B-Calculate Bonus
Q-Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "B":
        sales_input = "Enter sales: $"
        sales = float(input(sales_input))
        if sales > 1000:
            bonus_rate = 0.10
            bonus = sales * bonus_rate
            print("Result: ${:} ".format(bonus))
        elif sales < 1000:
            bonus_rate = 0.15
            bonus = sales * bonus_rate
            print("Result: ${:}".format(bonus))
        elif sales == 1000:
            bonus_rate = 0.15
            bonus = sales * bonus_rate
            print("Result: ${:} ".format(bonus))
        elif sales <= 0:
            print("Not a Real Sales Value")
            print(MENU)
            choice = input(">>> ").upper()
            print("Thank you.")
    else:
        print("INVALID OPTION")
        print(MENU)
        choice = input(">>> ").upper()













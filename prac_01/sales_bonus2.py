"""
CP1404/CP5632 - Practical - Suggested Solution
Sales bonus program
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus is $", bonus, sep='')
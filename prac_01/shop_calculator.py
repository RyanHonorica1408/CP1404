total = 0
item_amount = int(input("Enter item amount: "))
while item_amount < 0:
    print("Impossible amount ")
    item_amount = int(input("Enter item amount: "))
for i in range(item_amount):
    price = float(input("Enter item price:"))
    total += price
if total > 100:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(item_amount, total))
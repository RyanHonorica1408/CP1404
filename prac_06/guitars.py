
from guitar import Guitar

def main():
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = float(input("Cost: $"))
        guitar_being_added = Guitar(name, year, cost)
        guitars.append(guitar_being_added)
        print(guitar_being_added, "added")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    print("These are my guitars:")

    if guitars is not None:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                 {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
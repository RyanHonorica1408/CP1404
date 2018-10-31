"""
CP1404 Taxi Sim
Ryan Honorica
"""
from car import Car
from taxi import Taxi
from silverservicetaxi import SilverServiceTaxi

menu = "q)uit, c)hoose taxi, d)rive"

def main():
    bill_total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    print(menu)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            taxi_display(taxis)
            taxi_chosen = int(input("Choose taxi:"))
            used_taxi = taxis[taxi_chosen]
        elif menu_choice == "d":
            used_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            used_taxi.drive(distance_to_drive)
            cost = used_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(used_taxi.name, cost))
            bill_total += cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_total))
        print(menu)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill_total))
    print("Taxis are now:")
    display_taxis(taxis)



def taxi_display(taxis):
    for n, taxi in enumerate(taxis):
        print("{} - {}".format(n, str(taxi)))


def run_tests():
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    # drive bus (input/loop is oblivious to fuel)
    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()
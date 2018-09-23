from car import Car
from taxi import Taxi

Prius = Taxi("Prius 1", 100)
Prius.drive(40)
fare = Prius.get_fare()
print(Prius)
print(fare)
Prius.start_fare()
Prius.drive(100)
fare = Prius.get_fare()
print(Prius)
print(fare)

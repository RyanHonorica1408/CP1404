"""
CP1404/CP5632 Practical
Unreliable class
"""
from car import Car

class UnreliableCar(Car):
    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        Car.drive(self,distance)
        limit = randint(0,100)
        if  limit >= self.reliablity:
            distance =0
        distance_drived = super.drive(distance)
        return distance_drived




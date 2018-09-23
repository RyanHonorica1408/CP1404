from unreliablecar import UnreliableCar

    # create cars with different reliabilities
    good_car = UnreliableCar("Good", 100, 90)
    bad_car = UnreliableCar("Bad", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(bad_car)

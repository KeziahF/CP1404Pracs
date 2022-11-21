from prac_09.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Prius 1", 100, 70)
    car.drive(40)
    print(car)
    car.drive(100)
    print(car)


main()

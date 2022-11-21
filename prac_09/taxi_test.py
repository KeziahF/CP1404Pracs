from prac_09.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")


main()

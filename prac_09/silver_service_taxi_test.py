from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Prius 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")


main()

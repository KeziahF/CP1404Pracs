"""
CP1404 Prac 9
Silver Service Taxi test - runs tests for silver service taxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """simulation of functionality for silver service taxi class"""
    taxi = SilverServiceTaxi("Prius 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print(f"${fare}")


main()

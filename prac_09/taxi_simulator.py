from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """
Let's drive!
q)uit, c)hoose taxi, d)rive
"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Lets Drive!")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "q":
            print("Quit")
        elif choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            try:
                choice = int(input("Choose Taxi: "))
                current_taxi = taxis[choice]
                current_taxi.start_fare()
            except:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you drive")
            else:
                distance = int(input("Drive How Farm? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost: $ {cost:.2f}")
                bill_to_date += cost
        else:
            print("Invalid input, try again")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total Trip Cost: ${bill_to_date:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)

main()

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def celcius_to_farenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
    return()


def farenheit_to_celcius():
    farenheit = float(input("Farenheit: "))
    celcius = 5 / 9 * (farenheit - 32)
    print("Results: {:.2f} C".format(celcius))
    return()

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
         celcius_to_farenheit()
    elif choice == "F":
         farenheit_to_celcius()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")




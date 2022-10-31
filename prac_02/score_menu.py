MENU = """
Q - Quit
S - Score
"""

def user_result(score):
    if score < 0 or score >100:
        result = "Invalid Score"
    elif score < 50:
        result = "Bad"
    elif score >= 90:
        result = "Excellent"
    else:
        result ="Passable"
    print(result)
    return

def display_stars(score):
    score = round(score)
    for i in range(score):
        print('*', end="")

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "S":
            score = float(input("Score: "))
            if score>=0 and score <= 100:
                user_result(score)
                display_stars(score)
            else:
                print("Invalid score")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
        print("Thank you.")

main()


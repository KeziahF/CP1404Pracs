import random
numbers_in_game = 6
max_number = 45
min_number = 1
quick_pick = []

number_picks = int(input("How many quick picks would you like to generate?: "))
while number_picks < 0:
    print("Invalid number of games, try again")
    number_picks = int(input("How many quick picks would you like to generate?: "))

for i in range(number_picks):
    for i in range(numbers_in_game):
        quick_pick.append(random.randint(min_number, max_number))
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))
    quick_pick = []



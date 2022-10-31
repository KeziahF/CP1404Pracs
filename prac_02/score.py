"""
CP1404/CP5632 - Practical
"""
import random

def user_result(score):
    if score < 0 or score >100:
        result = "Invalid Score"
    elif score < 50:
        result = "Bad"
    elif score >= 90:
        result = "Excellent"
    else:
        result ="Passable"
    return result

def main():
    score = float(input("Enter score: "))
    result = user_result(score)
    print(result)

def random_score():
    score = random.randint(0, 100)
    result = user_result(score)
    print("random score = ", score, "result = ", result)


main()
random_score()

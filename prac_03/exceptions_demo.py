"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# A value error will occur when an invalid character is entered (e.g. a letter)
# A Zero division error will occur when a zero is entered as the denominator
# There are a number of ways to avoid a ZeroDivisionError e.g. just output the fraction (4/0),
# return the user to the entering of the values when the error occurs to try again
# or run a check before running the division to see if the entered values are valid
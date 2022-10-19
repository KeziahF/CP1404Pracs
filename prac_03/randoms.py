import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# the values 6,11 and 14 were produced when running the program,
# however, could have produced any integer between 5 and 20

# the values 5,3 and 3 were produced when running the program,
# however, could have produced any integer between 3 and 10 in steps of 2 e.g. 3,5,7,9
# therefore it could not have produced a 4

# the values 3.12...,3.73... and 5.48... were produced when running the program,
# however, could have produced any floating point value between 2.5 and 5.5
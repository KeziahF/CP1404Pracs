OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')

name = input("What is your name? ")

print(name, file=out_file)

out_file.close()

n_file = open("name.txt",'r')
user_name = n_file.read()
print("Your name is ", user_name)
n_file.close()

total = 0
file = open("numbers.txt",'r')
number1 = int(file.readline())
number2 = int(file.readline())
file.close()
total = number1 + number2
print(total)

num_file = open("numbers.txt", 'r')
total = 0
for line in num_file:
        number = int(line)
        total += number

num_file.close()
print(total)
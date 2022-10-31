num_items = int(input("Number of items: "))
price = 0
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

for i in range(num_items):
    price = price + float(input("Price of item: "))
if price > 100:
    discount = price*0.1
    price = price - discount

print(F"Total price for {num_items} is ${price:.2f}")

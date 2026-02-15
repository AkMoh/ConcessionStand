menu = {
    "Pizza": 2.99,
    "Hotdog": 3.50,
    "Slushee": 1.99,
    "Popcorn": 4.50,
    "Candy": 1.50,
}

order = []
total = 0

iteration = 1
print("-------FOOD STAND-------")
for y in menu:
    print(f"{iteration}. {y}")
    iteration += 1


while True:
    item = input("What would you like to purchase? (1-5): ")
    if item == "1":
        quantity = int(input("How many would you like?: "))
        for q in range(0, quantity):
            order.append("Pizza")
        total += menu.get("Pizza") * quantity
    elif item == "2":
        quantity = int(input("How many would you like?: "))
        for q in range(0, quantity):
            order.append("Hotdog")
        total += menu.get("Hotdog") * quantity

    elif item == "3":
        quantity = int(input("How many would you like?: "))
        for q in range(0, quantity):
            order.append("Slushee")
        total += menu.get("Slushee") * quantity

    elif item == "4":
        quantity = int(input("How many would you like?: "))
        for q in range(0, quantity):
            order.append("Popcorn")
        total += menu.get("Popcorn") * quantity

    elif item == "5":
        quantity = int(input("How many would you like?: "))
        for q in range(0, quantity):
            order.append("Candy")
        total += menu.get("Candy") * quantity

    else:
        print("Invalid input, try again.")
        continue
    item = input("Would you like anything else? (y/n): ")
    if item == "y":
        continue
    elif item == "n":
        break
    else:
        print("Invalid input, try again.")

print("-------YOUR ORDER------")
for y in order:
    print(f"x1 {y}")
print("-------YOUR TOTAL-------")
print(f"Your total is ${total:.2f}.")

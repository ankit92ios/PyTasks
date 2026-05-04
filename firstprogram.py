#program to create billing system at supermarket
while True:
    name = input("Enter customer's name: ")
    total = 0
    while True:
        print("enter amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name: ", name)
    print("Amount to be paid", total)
    print("-"*40)
    print("*** Hapyy Shopping ***")
    repeat = input("do you want to go to next customer? (yes/no): ")
    if repeat == "no" or repeat == "No":
            break 
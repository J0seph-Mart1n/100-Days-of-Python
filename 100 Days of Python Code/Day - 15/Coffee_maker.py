MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
#Report of Coffee maker
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#Function for expresso
def expresso():
    global resources
    #Checks if resources are available
    if resources['water']>0 and resources['milk']>0 and resources['coffee']>0:
        print("Insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        #Calculate total
        total = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
        if total<1.5:
            print("Sorry that's not enough money. Money refunded.")
        elif total>=1.5:
            #change calculation
            change = round(total-1.5, 2)
            print(f"Here is ${change} in change.")
            print("Enjoy your expresso ☕")
            #subtract resources quantity
            resources['money']+=1.5
            resources['water']-=50
            resources['coffee']-=18
    else:
        print("Insufficient resources!!")

#function for latte
def latte():
    global resources
    # Checks if resources are available
    if resources['water'] > 0 and resources['milk'] > 0 and resources['coffee'] > 0:
        print("Insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        # Calculate total
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if total < 2.5:
            print("Sorry that's not enough money. Money refunded.")
        elif total >= 2.5:
            # change calculation
            change = round(total - 2.5, 2)
            print(f"Here is ${change} in change.")
            print("Enjoy your latte ☕")
            # subtract resources quantity
            resources['money'] += 2.5
            resources['water'] -= 200
            resources['coffee'] -= 24
            resources['milk'] -= 150
    else:
        print("Insufficient resources!!")

#function for cappuccino
def cappuccino():
    global resources
    # Checks if resources are available
    if resources['water'] > 0 and resources['milk'] > 0 and resources['coffee'] > 0:
        print("Insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        # Calculate total
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if total < 3.0:
            print("Sorry that's not enough money. Money refunded.")
        elif total >= 3.0:
            # change calculation
            change = round(total - 3.0, 2)
            print(f"Here is ${change} in change.")
            print("Enjoy your cappuccino ☕")
            # subtract resources quantity
            resources['money'] += 3.0
            resources['water'] -= 250
            resources['coffee'] -= 24
            resources['milk'] -= 100
    else:
        print("Insufficient resources!!")

working = True
#main while loop for coffee maker
while working:
    order = input("What would you like? (expresso, latte, cappuccino): ")
    # if-else loop for different selections
    if order == "expresso":
        expresso()
    elif order == "latte":
        latte()
    elif order == "cappuccino":
        cappuccino()
    elif order == "report":
        report()
    elif order == "off":
        print("Coffee maker is turning off for maintenance.")
        working = False
    else:
        print("Invalid choice")


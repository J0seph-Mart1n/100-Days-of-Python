from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    coffees = menu.get_items()
    user_input = input(f"Enter your coffee {coffees}: ")
    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        moneymachine.report()
        coffeemaker.report()
    else:
        drink = menu.find_drink(user_input)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_is_on = True

money_machine.report()
coffee_maker.report()

while machine_is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like to order? {options}: ")

    if choice == 'off'.lower():
        machine_is_on = False

    elif choice == 'report'.lower():
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


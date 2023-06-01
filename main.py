from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
options = menu.get_items()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

is_coffee_machine_on = True
while is_coffee_machine_on:
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

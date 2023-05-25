from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachineObj=MoneyMachine()
CoffeeMakerObj=CoffeeMaker()
menu=Menu()
isOn=True


CoffeeMakerObj.report()
moneyMachineObj.report()

while isOn:
    options=menu.get_items()
    choice=input(f"What would you like? ({options})")
    if choice=='off':
        isOn=False
    elif choice=='report':
        CoffeeMakerObj.report()
        moneyMachineObj.report()
    else:
        drink=menu.find_drink(choice)
        if CoffeeMakerObj.is_resource_sufficient(drink) and moneyMachineObj.make_payment(drink.cost):
            CoffeeMakerObj.make_coffee(drink)
    

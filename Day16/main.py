from menu import Menu
from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from art import Art

money_machine = MoneyMachine()
coffee_machine = CoffeeMachine()
menu = Menu()


def main():
    is_on = True
    Art().print_logo()
    
    while is_on:

        options = menu.get_items()

        coffee_choice = input(f"What would you like? ({options}): ").lower()
        if coffee_choice == "off":
            is_on = False
            CoffeeMachine().switch_off_coffee_machine()
        elif coffee_choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            try:
                drink = menu.find_drink(coffee_choice)
                
                if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

            except Exception as e:
                print("Please enter the drink that is available. ")

if __name__ == "__main__":
    main()
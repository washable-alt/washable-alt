from Day15_Menu import MENU, resources 
from art import logo
import sys

# Dictionaries of dictionaries
#for item in MENU:
#    print(item)


total = 0
profit = 0

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted; False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def process_coins():
    """Returns the total calculated from coins inserted. """
    global total
    print("Please insert coins. ")
    number_of_quarters = input("How many quarters?: ")
    if number_of_quarters == 'off':
        switch_off_the_coffee_machine()
    total +=  int(number_of_quarters) * 0.25
    number_of_dimes = input("How many dimes?: ")
    if number_of_dimes == 'off':
        switch_off_the_coffee_machine()
    total +=  int(number_of_dimes) * 0.1
    number_of_nickles = input("How many nickles?: ")
    if number_of_nickles == 'off':
        switch_off_the_coffee_machine()
    total += int(number_of_nickles) * 0.05
    number_of_pennies = input("How many pennies?: ")
    if number_of_pennies == 'off':
        switch_off_the_coffee_machine()
    total += int(number_of_pennies) * 0.01
    return total


def check_resources(ingredients, resources):
  
    """Returns true when order is made and resources are enough"""
    is_enough = True
    for item in ingredients:
        
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough =  False
        return is_enough
    
    #if ingredients['water'] > resources['water']:
    #    print("Sorry there is not enough water. ")
    #elif ingredients['milk'] > resources['milk']:
    #    print("Sorry there is not enough milk. ")
    #elif ingredients['coffee'] > resources['coffee']:
    #    print("Sorry there is not enough coffee. ")


def switch_off_the_coffee_machine():
    print("Switching off the coffee machine...")
    sys.exit(0)

def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    return


def main():
    # Display logo
    print(logo)

    should_continue_making_coffee = True

    while should_continue_making_coffee:
        coffee_choice = input("What do you like? (expresso/latte/cappuccino): ").lower()
        if coffee_choice == 'off':
            should_continue_making_coffee = False
            switch_off_the_coffee_machine()
        # TODO 1. Print the report of all coffee machine resources
        elif coffee_choice == 'report':
            print_report(resources)
        else:
            try:
                drink = MENU[coffee_choice]
                ingredients = drink['ingredients']
                # TODO 2: Compare the resources to check if the ingredients are sufficient to make the cup of coffee
                if check_resources(ingredients, resources):
                    payments = process_coins()
                    # if transaction is successful, make coffee
                    if is_transaction_successful(payments, drink['cost']):
                        make_coffee(coffee_choice, ingredients)
            except Exception as e:
                print(f"{e} is not a correct input")

if __name__== "__main__":
    main()
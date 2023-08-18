class MenuItem:
    """Models each Menu Item."""
    #Ask yourself. What does a menu show? It needs a name, amount of water, milk and coffee required, and an associated cost
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
    
class Menu:
    """Models the Menu with drinks. """
    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("espresso",50,0,18,1.5),
            MenuItem("cappuccino",250,50,24,3)
        ]

    def get_items(self):
        """Returns all names of available menu items """
        options = ""
        for item in self.menu:
            #e.g latte/espresso/cappuccino
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if exist, else return None"""

        for item in self.menu:
            if order_name == item.name:
                return item
        print("Sorry that item is not available. ")
        
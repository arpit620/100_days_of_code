class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 500,
            "coffee": 200
        }
        self.menu = {
            "Espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "Latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "Cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
        }
        self.money = 0

    def check_resources(self, coffee_type):
        for item in self.menu[coffee_type]:
            if item != "cost" and self.resources[item] < self.menu[coffee_type][item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_payment(self, cost):
        print(f"The cost is ${cost}. Please insert coins.")
        total = int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
            self.money += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, coffee_type):
        for item in self.menu[coffee_type]:
            if item != "cost":
                self.resources[item] -= self.menu[coffee_type][item]
        print(f"Here is your {coffee_type}. Enjoy!")

    def dispense_coffee(self):
        print("Available options: Espresso, Latte, Cappuccino")
        choice = input("What would you like? ").capitalize()
        if choice in self.menu:
            if self.check_resources(choice):
                if self.process_payment(self.menu[choice]["cost"]):
                    self.make_coffee(choice)
        else:
            print("Invalid choice.")

# Example usage:
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.dispense_coffee()

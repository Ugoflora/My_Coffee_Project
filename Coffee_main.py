MENU = {
    "espresso": {
        "ingredients":{
            "water": 60,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 140,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 18
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}

def report():
    """print available resources"""
# for k, v in resources.items():
#          print(f"{k}:{v}")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profit: {resources['profit']}")

def is_resource_enough(order_ingredients): 
     """Return true if resources are sufficient and False if not sufficient"""
     for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
          print(f" sorry, there is insufficient {item}")
          return False
        else: 
            return True

def process_coins():
   """Return the total calculated from the coin inserted."""
   print("Please enter coins:")
   quaters = int(input("How many quaters?:"))* 0.25
   dimes = int(input("How many dimes?:"))* 0.1
   nickles = int(input("How many nickles?:"))* 0.05
   pennies= int(input("How many pennies?:"))* 0.01
   total = quaters + dimes + nickles + pennies 
   return total

def is_transaction_successful(money_received, drink_cost):
   """"Returns True if payment is accepted or return False if the payment is sufficient"""
   if money_received >= drink_cost:
      change = round(money_received - drink_cost, 2)
      print(f"Here is ${change} in change")
      resources["profit"] += drink_cost
      return True
   
def make_coffee(drink_name, order_ingredient):
    """Deducts the required ingredients from the resources"""
    for item in order_ingredient:
      resources[item] -= order_ingredient[item]

    print(f"Here is you {drink_name}, ENJOY!")
 
is_on = True

while is_on:
   choice = input("what would you like? (espresso/latte/cappuccino):").lower()
   if choice == "off":
      is_on = False
   elif choice == "report": 
     report()

   else:
      if is_resource_enough(MENU[choice]["ingredients"]):
         total = process_coins()  
      if is_transaction_successful(total, MENU[choice]["cost"]):
           make_coffee(choice, MENU[choice]["ingredients"])     
#-----------------------------------------------------
#               Setup Local Development              |
#          Environment & Coffee Machine Project      |   
#                   Use Pycharm                      |
#-----------------------------------------------------

# 1. Makes 3 hot flavours
# |     Espresso      |   50 ml Water + 18 g Coffee                  |   $1.50   |
# |     Latte         |   200 ml Water + 24 g Coffee + 150 ml Milk   |   $2.50   |
# |     Cappuccino    |   250 ml Water + 24 g Coffee + 100 ml Milk   |   $3.00   |

# TODO: 2. Check resources sufficient to make drink order.
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
        "cost": 3.00,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report of all coffee machine resources.
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item] :
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    """Returns the total calculated from cois inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item]  -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_one = True
while is_one:
    choice = input("What would you like? (espresso/ Latte/ Cappuccino): ")
    if choice == "off":
        is_one = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]) :
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]) :
                make_coffee(choice, drink["ingredients"])


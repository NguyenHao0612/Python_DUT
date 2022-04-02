#---------------------------------------------------
#           Object Oriented Programming
#           (Lap Trinh Huong Doi Tuong )
#---------------------------------------------------
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle&msclkid=891aba78a79911ecbc42cfdfe29ae1a5
# 1. Constructing Objects ( Xay Dung Doi Tuong )
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# 2. Object Attributes ( Thuoc Tinh Doi Tuong )
# Object | attribute
#     car.speed 

# 3. Object Methods ( Phuong Thuc cua Doi Tuong )
#       Object | Method
#           car.stop()

#---------------------------------------------------
#               Python Packages ( Goi)
#---------------------------------------------------

print("| Pokemon Name | Type |")

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire", ])

table.align = "L"

print(table)

#----------------------------------------------------
#                   Coffee Machine                  |
#----------------------------------------------------
#   Program Requirements            |   Yeu cau Chuong Trinh
#   1. Print report.                |   Hien Thi Thong Bao
#   2. Check resources sufficient?  |   Kiem Tra Tai Nguyen
#   3. Process coins.               |   Xu Ly Tien Xu
#   4. Check transaction successful?|   Kiem Tra Giao Dich
#   5. Make Coffee.                 |   Lam Coffee
#   meu.py  |   momey_machine.py    |   coffee_maker.py

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingerdients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingerdients and is_payment_successful :
            coffee_maker.make_coffee(drink)

# pycharm là IDE víual studio code là editor
# IDE thì tích hợp môi trường , editor chỉ soạn thảo
#------------------------------------------------
# Functions with outputs

def format_name(f_name, l_name):

    if f_name == "" or l_name == "" :
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(f"Result: {formated_f_name} {formated_l_name}")
    

print(format_name(input("What is your first name? "), input("What is your last name? ")))

#-------------------------------------------------
# Days in Month Exercise

def is_leap(year):
    if year % 4 ==0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # if month > 12 or month < 1 :
    #     return "Invalid month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2 :
        return 29
    return month_days[month - 1 ]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#------------------------------------------------------
#  Calculator

from art import logo_calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract 
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    
    print(logo_calculator)
    num1 = float(input("What's the first number?: "))

    for symbol in operations :
        print(symbol)
    should_continue = True

    while should_continue:

        operations_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1 , num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input("Exit ? 'yes' or 'no'. ") == "yes":
            break

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

    print("GoodBye")
    
        

calculator()
#--------------------------------------------------------------


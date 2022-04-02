# Data types
print("Hello"[0])

#-----------------------------------------------------------
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
a = float(123)
print(type(a))
print(str(49)+str(100))

#------------------------------------------------------------
two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)
result_digit = int(first_digit)+int(second_digit)
print(result_digit)

#-----------------------------------------------------------
print(3*(3+3)/3-3)

#-----------------------------------------------------------
# BMI = weight(kg) / (hight(m))^2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight)/float(height)**2
BMI_as_int = int(BMI)
print(BMI_as_int)

#-----------------------------------------------------------
print(round(8/3, 2))
score = 0
score += 1
height = 1.8
isWinning = True
print("your score is ")
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#-----------------------------------------------------------
age  = input("What is your current age? ")
age_as_int = int(age)
years_remaining  = 90 - age_as_int
days_remaining  = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message =f"You have {days_remaining} days , {weeks_remaining} weeks, {months_remaining} months"
print(message)

#-----------------------------------------------------------
# if the bill was $150.00 split between 5 people with 12% tip
# each person should pay (150.00 / 5) * 1.12
# round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person , 2)
print(f"Each person should pay $ {final_amount} ")
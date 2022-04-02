#--------------------------------------------------------
# Random
import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
print("-------------------------------------")

#---------------------------------------------------------
# Heads or Tails
#import random 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0,1)
if random_side == 1 :
    print("Heads")
else:
    print("Tails")

#--------------------------------------------------------
# List
states_of_america = ["Delaware", "Jack Bauer Land", "Hawaii"]
print(states_of_america[2])
states_of_america.append("Pennsylnavia")
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)

#----------------------------------------------------------
# who's Paying 
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's name, seperated by a comma. ")
names = namesAsCSV.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today! ")

#---------------------------------------------------------------------------
#
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Straberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

#-----------------------------------------------------------------------------
# Treasure Map
row1 = [" "," "," "]        # 0 1 2
row2 = [" "," "," "]        # 1 
row3 = [" "," "," "]        # 2
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure")

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizonal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#--------------------------------------------------------------
# keo Bua Bao
import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: \n")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0 :
    print("You types an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")



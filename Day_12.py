#-----------------------------------------------------
#           Namespaces: Local vs. Global Scope       |
#-----------------------------------------------------

# Scope
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Loacl Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()
# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5 :
#         new_enemy = enemies[0]

#     print(new_enemy)

# How to Modify Variable with Global Scope

# enemies = 1

# def increse_enemies():
    
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increse_enemies()
# print(f"enemies outside function: {enemies}")

# Python Constants & Global Scope
# Global Contants

#-----------------------------------------------------
#                   Guess The Number                 |
#-----------------------------------------------------
from random import randint
from art import logo_Guess_The_Number
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Check answer against guess. Returns the number of turns remaning"""
    if guess > answer :
        print("Two High. ")
        return turns - 1
    elif guess < answer :
        print("Two Low. ")
        return turns -1 
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy" :
        # global turns
        # turns = EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo_Guess_The_Number)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    #print(f"Pssst, the correct answer is {answer} ")

    turns = set_difficulty()
    
    # Repeat the guessing functionality if they got it wrong
    guess = 0
    while guess != answer:

        print(f"You have {turns} attemps remainning to guess the number. ")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0 :
            print(f"You've run out of guesses, you lose.\nAnswer is {answer} ")
            return
        elif guess != answer:
            print("Guess again.")
# Track the number of turns and reduce by 1 if they get it wrong.

game()

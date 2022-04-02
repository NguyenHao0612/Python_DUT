#-----------------------------------------------
#               Hangman Project
#-----------------------------------------------
#             +---------++
#             |         ||
#             |         ||
#             O         || 
#            /|\        || 
#             |         ||
#            / \        ||
#                       ||
#_______________________||______________________

import random
from hangman_words import words_list

chosen_word = random.choice(words_list)
lives = 6
from hangman_art import logo, stages
print(logo)

print(f"Pssst, the solution is {chosen_word}.")

display = []
word_lenght = len(chosen_word)
for letter in range(word_lenght):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess} ")

    for position in range(word_lenght):
        letter = chosen_word[position]
        #print(f"Current position: {position} \nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You a life")
        lives -= 1
        if lives == 0 :
            end_of_game = True
            print("You Lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[6- lives])

#-------------------------------------------------------------------

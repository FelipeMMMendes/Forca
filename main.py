from hangman_words import word_list
from hangman_art import *

import random
import os

#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
traces = []
tela = ''

print(logo)

for n in chosen_word:
    traces.append('_')

print()
print(' '.join(traces))
traces = ''.join(traces)
 
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

lives = 6

while lives != 0:
    print(stages[lives])
    guess = str(input("Guess a letter: ").lower())
    
    os.system('cls')
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    traces = list(traces)
    checkTraces = len(traces)
    checkError = chosen_word.count(guess)

    for n in range(len(chosen_word)):
        letter = chosen_word[n]
        if letter == guess:
          traces[n] = guess
          tela = ' '.join(traces)

        elif checkError == 0:
          lives -= 1
          checkError = 1  

        checkTraces = traces.count('_')
        
        if checkTraces == 0:
          print(tela)
          print("The player won!")
          exit()

        elif lives == 0:
          print(stages[lives])
          print("the word was: " + ''.join(chosen_word))
          print("You lose!")
          exit()  

    print(tela)
    
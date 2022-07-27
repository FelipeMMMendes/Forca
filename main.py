import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(chosen_word)
traces = []
tela = ''

for n in chosen_word:
    traces.append('_')

traces = ''.join(traces)

print(f"\n{traces}")  
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

lives = 6

while lives != 0:
    print(stages[lives])
    print(tela)
    guess = str(input("Guess a letter: ").lower())
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    traces = list(traces)
    checkTraces = len(traces)
    checkError = chosen_word.count(guess)

    for n in range(len(chosen_word)):
        letter = chosen_word[n]
        if letter == guess:
          traces[n] = guess
          tela = ''.join(traces)

        elif checkError == 0:
          lives -= 1
          checkError = 1

        checkTraces = traces.count('_')
        
        if checkTraces == 0:
          print("The player won!")
          exit()

        elif lives == 0:
          print(stages[0])
          print("You lose!")
          exit()  

    
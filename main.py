import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(chosen_word)
traces = []

for n in chosen_word:
    traces.append('_')

traces = ' '.join(traces)

print(traces)  
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = str(input("Guess a letter: ").lower())
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for w in chosen_word:
    if guess == w:
        print(w)
        pos = chosen_word.index(guess)
        traces = list(traces)
        traces[pos] = guess
    else:
        print("WRONG")    

print(traces)
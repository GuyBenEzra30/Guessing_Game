import random
import string
from nltk.corpus import words
import nltk

game_title = "The Guessing Game"

nltk.download('words') # download the words corpus if not already downloaded


def generate_real_words(count, length):
    word_list = [word.lower() for word in words.words() if len(word) == length] # Get all words of the specified length
    return random.sample(word_list, count) 

word_bank = []

# Load or generate a word bank
try:
    with open("Words.txt") as word_file:
        word_bank = [line.strip().lower() for line in word_file] # Load the word bank from the file

except FileNotFoundError:
    word_bank = [] 

if not word_bank:
    print("No valid words found. Generating a new file with real words...")
    word_bank = generate_real_words(10, 5)
    
    with open("Generated_Words.txt", "w") as gen_file: # Save the word bank to a file
        gen_file.write("\n".join(word_bank))
    print("Generated_Words.txt created with 10 real five-letter words.") 


random_guess = random.choice(word_bank)

misplaced = []
incorrect = []
max_guesses = 5
guesses_taken = 0

print("\nWelcome to", game_title)
print("\nThe word has", len(random_guess), "letters")
print("You have", max_guesses, "guesses.\n")

# Main game loop

while guesses_taken < max_guesses:
    guess = input("Guess a word: ").lower() # convert the guess to lowercase.

    if not guess.isalpha():
        print("Invalid guess. Please use only letters.")
        continue
         
    elif len(guess) != len(random_guess): 
        print(f"Invalid guess. Please enter a word with 5 letters.")
        continue

    # Track each character of the guess
    
    index = 0
    
    for count in guess:
        if count == random_guess[index]:
            print(count, end=" ")
            if count not in misplaced: 
                misplaced.append(count)
                
        elif count in random_guess:
            if count not in misplaced: # if the letter is not in misplaced, add it to misplaced.
                misplaced.append(count)
            print("_", end=" ")
            
        else:
            if count not in incorrect: # if the letter is not in incorrect, add it to incorrect.
                incorrect.append(count)
            print("_", end=" ")

        index += 1

    print("\n-------------------")
    print("Misplaced letters: ", misplaced)
    print("Incorrect letters: ", incorrect)
    print("-------------------\n")

    guesses_taken += 1

    if guess == random_guess:
        print("Congratulations, you won!")
        break

    if guesses_taken == max_guesses:
        print("You ran out of guesses. The word was", random_guess)
        break

    print("You have", max_guesses - guesses_taken, "guesses left.")

import random

game_title = "The Guessing Game"

word_bank = []

with open("Words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower()) 

if not word_bank:
    print("The word bank is empty!")
    exit()

random_guess = random.choice(word_bank)

misplaced = []
incorrect = []
max_guesses = 5
guesses_taken = 0

print("\nWelcome to", game_title)
print("\nThe word has", len(random_guess), "letters")
print("You have", max_guesses, "guesses.\n")

while guesses_taken < max_guesses:
    guess = input("Guess a word: ").lower()

    if not guess.isalpha():
        print("Invalid guess. Please use only letters.")
        continue
        
    elif len(guess) != len(random_guess):
        print(f"Invalid guess. Please enter a word with {len(random_guess)} letters.")
        continue

    index = 0
    
    for count in guess:
        if count == random_guess[index]:
            print(count, end=" ")
            if count not in misplaced:
                misplaced.append(count)
                
        elif count in random_guess:
            if count not in misplaced:
                misplaced.append(count)
            print("_", end=" ")
            
        else:
            if count not in incorrect:
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

import random
import string
from nltk.corpus import words
import nltk
import tkinter as tk
from tkinter import messagebox

# Initialize NLTK and download the words corpus if not already downloaded
nltk.download('words')

def generate_real_words(count, length):
    word_list = [word.lower() for word in words.words() if len(word) == length]
    return random.sample(word_list, count)

# Load or generate a word bank
try:
    with open("Words.txt") as word_file:
        word_bank = [line.strip().lower() for line in word_file]
except FileNotFoundError:
    word_bank = []

if not word_bank:
    word_bank = generate_real_words(10, 5)
    with open("Generated_Words.txt", "w") as gen_file:
        gen_file.write("\n".join(word_bank))

random_guess = random.choice(word_bank)
misplaced = []
incorrect = []
max_guesses = 5

def check_guess():
    global max_guesses, misplaced, incorrect, random_guess

    guess = guess_entry.get().lower()
    result_label.config(text="")

    if not guess.isalpha():
        messagebox.showerror("Invalid Input", "Please enter only letters.")
        return

    if len(guess) != len(random_guess):
        messagebox.showerror("Invalid Input", f"Please enter a {len(random_guess)}-letter word.")
        return

    result = []
    misplaced.clear()
    incorrect.clear()

    for i, char in enumerate(guess):
        if char == random_guess[i]:
            result.append(char.upper())
        elif char in random_guess:
            if char not in misplaced:
                misplaced.append(char)
            result.append("_")
        else:
            if char not in incorrect:
                incorrect.append(char)
            result.append("_")

    result_label.config(text=" ".join(result)) # Display the result
    misplaced_label.config(text="Misplaced Letters: " + ", ".join(misplaced)) # Display misplaced letters
    incorrect_label.config(text="Incorrect Letters: " + ", ".join(incorrect)) # Display incorrect letters

    if guess == random_guess:
        messagebox.showinfo("Congratulations", "You guessed the word correctly!")
        reset_game()
    else:
        global guesses_taken
        guesses_taken += 1
        if guesses_taken == max_guesses:
            messagebox.showerror("Game Over", f"You've run out of guesses. The word was {random_guess}.")
            reset_game()
        else:
            remaining_label.config(text=f"Guesses Remaining: {max_guesses - guesses_taken}")

def reset_game():
    global random_guess, misplaced, incorrect, guesses_taken
    random_guess = random.choice(word_bank)
    misplaced.clear()
    incorrect.clear()
    guesses_taken = 0
    result_label.config(text="")
    misplaced_label.config(text="Misplaced Letters: ") # Display misplaced letters
    incorrect_label.config(text="Incorrect Letters: ") # Display incorrect letters
    remaining_label.config(text=f"Guesses Remaining: {max_guesses}")
    guess_entry.delete(0, tk.END)

guesses_taken = 0

# Create the main application window
root = tk.Tk()
root.title("The Guessing Game")
root.geometry("400x400")
root.resizable(False, False)

# Create and place widgets
title_label = tk.Label(root, text="The Guessing Game", font=("Helvetica", 16))
title_label.pack(pady=10)

description_label = tk.Label(root, text=f"Guess the {len(random_guess)}-letter word!")
description_label.pack(pady=5)

remaining_label = tk.Label(root, text=f"Guesses Remaining: {max_guesses}")
remaining_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

misplaced_label = tk.Label(root, text="Misplaced Letters: ")
misplaced_label.pack(pady=5)

incorrect_label = tk.Label(root, text="Incorrect Letters: ")
incorrect_label.pack(pady=5)

guess_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
guess_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

# Run the application
root.mainloop()
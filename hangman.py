import random

def hangman():
    word = random.choice(['python', 'hangman', 'developer'])
    guessed = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        display = ' '.join(letter if letter in guessed else '_' for letter in word)
        print(f"\nWord: {display}\nAttempts left: {attempts}")

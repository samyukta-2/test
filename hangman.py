import random

def hangman():
    word = random.choice(['python', 'hangman', 'developer'])
    guessed = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        display = ' '.join(letter if letter in guessed else '_' for letter in word)
        print(f"\nWord: {display}\nAttempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed or not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Try again.")
            continue

        guessed.add(guess)
        if guess not in word:
            attempts -= 1
            print("Incorrect!")

        if set(word).issubset(guessed):
            print(f"You win! The word was: {word}")
            return

    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()


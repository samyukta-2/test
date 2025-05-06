import random

def higher_lower_game():
    print("Welcome to the Higher-Lower Game!")
    secret_number = random.randint(1, 100)  # The secret number is between 1 and 100
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
        if guess.lower() == 'exit':
            print(f"You gave up! The number was {secret_number}.")
            break
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue
         guess = int(guess)
        attempts += 1

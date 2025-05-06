import random

def generate_number():
    """Generate a 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def calculate_cows_and_bulls(secret, guess):
    """Calculate the number of cows and bulls."""
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - cows
    return cows, bulls

def play_cows_and_bulls():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_number()
    attempts = 0

     while True:
        guess = input("Enter your 4-digit guess (or type 'exit' to quit): ")
         if guess.lower() == 'exit':
            print(f"You gave up! The number was {secret_number}.")
            break
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        attempts += 1
        cows, bulls = calculate_cows_and_bulls(secret_number, guess)
        print(f"{cows} cow(s), {bulls} bull(s)")
        if cows == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

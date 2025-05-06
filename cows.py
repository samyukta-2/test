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

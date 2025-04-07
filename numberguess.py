import random
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed it right!")
        break

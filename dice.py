import random

def roll_dice():
    return random.randint(1, 6)
while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print(f"You rolled a {result} 🎲")


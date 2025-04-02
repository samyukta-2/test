import random

def main():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice!")
        return
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif (user, computer) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()

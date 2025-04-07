import random
board = {
    3: 22,  5: 8,   11: 26,  20: 29,
    27: 1,  21: 9,  17: 4,   19: 7  
}
player1 = 0
player2 = 0
def roll():
    return random.randint(1, 6)

def move(player):
    input("Press Enter to roll the dice...")
    dice = roll()
    print(f"Rolled: {dice}")
    player += dice
    if player in board:
        player = board[player]
    if player > 30:
        player = 30
    print(f"Now at: {player}\n")
    return player

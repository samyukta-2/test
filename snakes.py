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
while True:
    print("Player 1's turn")
    player1 = move(player1)
    if player1 == 30:
        print("Player 1 wins!")
        break

    print("Player 2's turn")
    player2 = move(player2)
    if player2 == 30:
        print("Player 2 wins!")
        break

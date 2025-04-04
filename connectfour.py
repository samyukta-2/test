ROWS, COLS = 6, 7

board = [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLS)))

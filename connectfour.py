ROWS, COLS = 6, 7

board = [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLS)))
def drop(col, piece):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = piece
            return r

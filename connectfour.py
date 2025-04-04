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
def check_win(r, c, piece):
    dirs = [(1,0), (0,1), (1,1), (1,-1)]
    for dr, dc in dirs:
        count = 1
        for i in range(1, 4):
            nr, nc = r + dr*i, c + dc*i
            if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == piece:
                count += 1
            else:
                break
        for i in range(1, 4):
            nr, nc = r - dr*i, c - dc*i
            if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == piece:
                count += 1
            else:
                break
        if count >= 4:
            return True
    return False
turn = 0
while True:
    print_board()
    col = int(input(f"Player {turn+1} ({'X' if turn == 0 else 'O'}), pick column (0-{COLS-1}): "))
    if 0 <= col < COLS and board[0][col] == " ":
        row = drop(col, 'X' if turn == 0 else 'O')
        if check_win(row, col, board[row][col]):
            print_board()
            print(f"Player {turn+1} wins!")
            break
        turn = 1 - turn
    else:
        print("Try another column.")

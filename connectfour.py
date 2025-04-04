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

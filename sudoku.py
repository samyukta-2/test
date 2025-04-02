def is_valid(board, r, c, n):
    return all(n != board[r][i] for i in range(9)) and \
           all(n != board[i][c] for i in range(9)) and \
           all(n != board[r//3*3 + i//3][c//3*3 + i%3] for i in range(9))

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board): return True
                        board[r][c] = 0
                return False
    return True

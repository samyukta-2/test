import random

def create_board(size, num_mines):
    mines = set(random.sample([(r, c) for r in range(size) for c in range(size)], num_mines))
    return [['M' if (r, c) in mines else ' ' for c in range(size)] for r in range(size)], mines

def count_adjacent_mines(board, row, col, size):
    return sum(board[r][c] == 'M' for r in range(max(0, row-1), min(size, row+2)) for c in range(max(0, col-1), min(size, col+2)))
def reveal(board, display, row, col, size):
    if display[row][col] != '_': return
    count = count_adjacent_mines(board, row, col, size)
    display[row][col] = str(count) if count else ' '
    if count == 0:
        for r in range(max(0, row-1), min(size, row+2)):
            for c in range(max(0, col-1), min(size, col+2)):
                reveal(board, display, r, c, size)
def play_minesweeper(size=5, num_mines=5):
    board, mines = create_board(size, num_mines)
    display = [['_'] * size for _ in range(size)]

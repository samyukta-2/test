import random

def create_board(size, num_mines):
    mines = set(random.sample([(r, c) for r in range(size) for c in range(size)], num_mines))
    return [['M' if (r, c) in mines else ' ' for c in range(size)] for r in range(size)], mines

def count_adjacent_mines(board, row, col, size):
    return sum(board[r][c] == 'M' for r in range(max(0, row-1), min(size, row+2)) for c in range(max(0, col-1), min(size, col+2)))

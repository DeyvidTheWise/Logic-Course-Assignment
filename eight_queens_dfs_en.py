def is_safe(board, row, col):
    # Check for horizontal attacks
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for diagonal attacks on top left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for diagonal attacks on bottom left
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_eight_queens_dfs(board, col):
    # If all queens are placed, the problem is solved
    if col >= len(board):
        return True

    # Go through all rows of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_eight_queens_dfs(board, col + 1):
                return True
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

board = [[0 for _ in range(8)] for _ in range(8)]

if solve_eight_queens_dfs(board, 0):
    print("Solution found:")
    print_board(board)
else:
    print("No solution found")
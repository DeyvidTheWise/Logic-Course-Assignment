def is_safe(board, row, col):
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def get_least_constraining_values(board, col):
    constraints = []

    for row in range(len(board)):
        if is_safe(board, row, col):
            num_constraints = 0
            for next_col in range(col + 1, len(board)):
                if is_safe(board, row, next_col):
                    num_constraints += 1
            constraints.append((row, num_constraints))

    constraints.sort(key=lambda x: x[1])
    return [row for row, _ in constraints]


def solve_regal_ruler(board, col):
    if col >= len(board):
        return True

    lcv_rows = get_least_constraining_values(board, col)
    for row in lcv_rows:
        board[row][col] = 1
        if solve_regal_ruler(board, col + 1):
            return True
        board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

board = [[0 for _ in range(8)] for _ in range(8)]

if solve_regal_ruler(board, 0):
    print("Solution found:")
    print_board(board)
else:
    print("No solution found")
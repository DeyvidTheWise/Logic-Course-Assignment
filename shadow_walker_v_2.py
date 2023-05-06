import random

def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        next_x, next_y = x + pos_x[i], y + pos_y[i]
        if 0 <= next_x < 8 and 0 <= next_y < 8 and chess_board[next_x][next_y] == 0:
            possibilities.append((next_x, next_y))

    return possibilities

def print_board():
    for row in chess_board:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()

def solve_randomized_dynamic_backtracking(x, y, move_count=1):
    if move_count == 64:
        return True

    next_moves = get_possibilities(x, y)
    # Apply the Warnsdorff rule by sorting the moves based on the number of onward moves
    next_moves.sort(key=lambda move: len(get_possibilities(move[0], move[1])))

    for next_x, next_y in next_moves:
        chess_board[next_x][next_y] = move_count + 1
        if solve_randomized_dynamic_backtracking(next_x, next_y, move_count + 1):
            return True
        chess_board[next_x][next_y] = 0  # Backtrack

    return False

for _ in range(100):  # You can adjust the number of attempts
    # Reset the chessboard
    chess_board = [[0 for _ in range(8)] for _ in range(8)]

    # Choose random starting position
    start_x, start_y = random.randint(0, 7), random.randint(0, 7)
    chess_board[start_x][start_y] = 1

    # Solve the Knight's Tour problem using Randomized Dynamic Backtracking with Warnsdorff's Rule
    if solve_randomized_dynamic_backtracking(start_x, start_y):
        print("Solution found with random starting position:")
        print_board()
        break
else:
    print("No solution found after multiple attempts")
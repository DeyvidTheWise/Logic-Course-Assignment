import random

def print_board():
    for row in chess_board:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()

def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []

    for i in range(8):
        next_x, next_y = x + pos_x[i], y + pos_y[i]
        if 0 <= next_x < 8 and 0 <= next_y < 8 and chess_board[next_x][next_y] == 0:
            possibilities.append((next_x, next_y))

    return possibilities

def knight_tour_dfs(x, y, move_count):
    if move_count > 64:
        return True

    next_moves = get_possibilities(x, y)
    next_moves.sort(key=lambda move: len(get_possibilities(move[0], move[1])))  # Warnsdorff rule

    for next_x, next_y in next_moves:
        chess_board[next_x][next_y] = move_count
        if knight_tour_dfs(next_x, next_y, move_count + 1):
            return True
        chess_board[next_x][next_y] = 0  # Backtrack

    return False

# Reset the chessboard
chess_board = [[0 for _ in range(8)] for _ in range(8)]

# Choose random starting position
start_x, start_y = random.randint(0, 7), random.randint(0, 7)
chess_board[start_x][start_y] = 1

# Solve the Knight's Tour problem using DFS with Warnsdorff's Rule
if knight_tour_dfs(start_x, start_y, 2):
    print("Solution found with random starting position:")
    print_board()
else:
    print("No solution found")
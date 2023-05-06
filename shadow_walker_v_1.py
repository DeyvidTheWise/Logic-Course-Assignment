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

def solve_randomized_dynamic_backtracking():
    move_number = 2
    x, y = 0, 0
    while move_number <= 64:
        pos = sorted(get_possibilities(x, y), key=lambda p: len(get_possibilities(p[0], p[1])))
        
        if len(pos) > 1:
            random.shuffle(pos[:3])

        if not pos:
            break

        x, y = pos[0]
        chess_board[x][y] = move_number
        move_number += 1

    if move_number == 65:
        print("Solution found:")
        print_board()
    else:
        print("No solution found")

for _ in range(100):
    chess_board = [[0 for _ in range(8)] for _ in range(8)]

    start_x, start_y = random.randint(0, 7), random.randint(0, 7)
    chess_board[start_x][start_y] = 1

    solve_randomized_dynamic_backtracking()

    if all(chess_board[i][j] != 0 for i in range(8) for j in range(8)):
        break
else:
    print("No solution found after multiple attempts")
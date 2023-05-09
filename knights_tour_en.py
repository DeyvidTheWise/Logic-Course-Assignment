# Initialize the chess board
def create_board(start_x, start_y):
    chess_board = [[0 for _ in range(8)] for _ in range(8)]
    chess_board[start_x][start_y] = 1
    return chess_board

start_x, start_y = 0, 0
chess_board = create_board(start_x, start_y)

# Funktion zum Ausgeben des Schachbretts
def print_board():
    for row in chess_board:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()

# Function to get the possible moves for the knight at position (x, y)
def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1,-2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x+pos_x[i] >= 0 and x+pos_x[i] <= 7 and y+pos_y[i] >= 0 and y+pos_y[i] <= 7 and chess_board[x+pos_x[i]][y+pos_y[i]] == 0:
            possibilities.append([x+pos_x[i], y+pos_y[i]])

    return possibilities

# Function to solve the knight's tour problem
def solve():
    counter = 2
    x = 0
    y = 0
    for _ in range(63):
        pos = get_possibilities(x, y)
        minimum = pos[0]
        for p in pos:
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1

# Solve the knight's tour problem and print the resulting chess board
solve()
print_board()
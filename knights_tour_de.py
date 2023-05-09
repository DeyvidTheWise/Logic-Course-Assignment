# Initialisiere das Schachbrett
chess_board = [[1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

# Funktion zum Ausgeben des Schachbretts
def print_board():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end=" ")
        print("\n")

# Funktion zum Ermitteln der möglichen Züge für den Springer in der Position (x, y)
def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1,-2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x+pos_x[i] >= 0 and x+pos_x[i] <= 7 and y+pos_y[i] >= 0 and y+pos_y[i] <= 7 and chess_board[x+pos_x[i]][y+pos_y[i]] == 0:
            possibilities.append([x+pos_x[i], y+pos_y[i]])
    
    return possibilities

# Funktion zum Lösen des Rittertourenproblems
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

# Löse das Rittertourenproblem und gebe das resultierende Schachbrett aus
solve()
print_board()
import random

# Drucke das Schachbrett (Print the chessboard)
def print_board(board):
    for row in board:
        for cell in row:
            print(f"{cell:2}", end=" ")
        print()

# Hole die möglichen Züge
def get_possibilities(x, y, board):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []

    for i in range(8):
        next_x, next_y = x + pos_x[i], y + pos_y[i]
        if 0 <= next_x < 8 and 0 <= next_y < 8 and board[next_x][next_y] == 0:
            possibilities.append((next_x, next_y))

    return possibilities

# Berechne die Distanz zum Zentrum
def distance_to_center(x, y):
    return abs(3.5 - x) + abs(3.5 - y)

# Kombiniere Warnsdorffs Regel und Zentrumsdistanzpriorisierung
def combined_heuristic(x, y, move_count, board):
    if move_count > 64:
        return True

    next_moves = get_possibilities(x, y, board)
    next_moves.sort(key=lambda move: (len(get_possibilities(move[0], move[1], board)), distance_to_center(move[0], move[1])))

    for next_x, next_y in next_moves:
        board[next_x][next_y] = move_count
        if combined_heuristic(next_x, next_y, move_count + 1, board):
            return True
        board[next_x][next_y] = 0  # Zurückverfolgen

    return False

# Schachbrett zurücksetzen
chess_board = [[0 for _ in range(8)] for _ in range(8)]

# Zufällige Startposition wählen 
start_x, start_y = random.randint(0, 7), random.randint(0, 7)
chess_board[start_x][start_y] = 1

# Löse das Springertour-Problem mit dem ShadowWalker-Algorithmus
if combined_heuristic(start_x, start_y, 2, chess_board):
    print("Lösung gefunden mit zufälliger Startposition")
    print_board(chess_board)
else:
    print("Keine Lösung gefunden")

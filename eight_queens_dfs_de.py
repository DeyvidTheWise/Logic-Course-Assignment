def is_safe(board, row, col):
    # Prüfe auf horizontale Angriffe
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Prüfe auf diagonale Angriffe oben links
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Prüfe auf diagonale Angriffe unten links
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_eight_queens_dfs(board, col):
    # Wenn alle Königinnen platziert sind, ist das Problem gelöst
    if col >= len(board):
        return True

    # Gehe durch alle Zeilen der aktuellen Spalte
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
    print("Lösung gefunden:")
    print_board(board)
else:
    print("Keine Lösung gefunden")

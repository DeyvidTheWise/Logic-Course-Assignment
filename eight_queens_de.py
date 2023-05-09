# Initialisiere das Schachbrett
chess_board = [[0]*8 for _ in range(8)]

# Prüft, ob eine Königin in den angegebenen Koordinaten (i, j) angegriffen wird
def attack(i, j):
    # Prüft horizontale und vertikale Angriffe
    for k in range(0,8):
        if chess_board[i][k]==1 or chess_board[k][j]==1:
            return True
    # Prüft diagonale Angriffe
    for k in range(0,8):
        for l in range(0,8):
            if (k+l==i+j) or (k-l==i-j):
                if chess_board[k][l]==1:
                    return True
    return False

# Löst das Eight-Queens-Problem mit Backtracking und Forward Checking
def solve(n):
    # Wenn alle Königinnen platziert sind, ist das Problem gelöst
    if n==0:
        return True
    # Gehe durch alle Zellen des Schachbretts
    for i in range(0,8):
        for j in range(0,8):
            # Wenn die Zelle nicht angegriffen wird und keine Königin enthält
            if (not(attack(i,j))) and (chess_board[i][j]!=1):
                # Platziere eine Königin in der Zelle
                chess_board[i][j] = 1
                # Rufe rekursiv die Funktion auf, um die verbleibenden Königinnen zu platzieren
                if solve(n-1)==True:
                    return True
                # Wenn die Platzierung fehlschlägt, entferne die Königin aus der Zelle
                chess_board[i][j] = 0
    return False

# Löse das Eight-Queens-Problem
solve(8)

# Drucke das resultierende Schachbrett
for i in chess_board:
    print(i)
from collections import deque

def bfs_solve():
    # Initialisiere die Warteschlange mit einem leeren Schachbrett und der ersten Spalte
    queue = deque([([], 0)])
    
    while queue:
        # Entferne das erste Element aus der Warteschlange
        queens, column = queue.popleft()
        
        # Wenn alle 8 Königinnen platziert sind, ist das Problem gelöst
        if column == 8:
            return queens

        # Gehe alle Zeilen der aktuellen Spalte durch
        for row in range(8):
            # Prüfe, ob die Platzierung der Königin gültig ist
            if is_valid(queens, row, column):
                # Erstelle eine Kopie der aktuellen Königinnen und füge die neue Königin hinzu
                new_queens = queens.copy()
                new_queens.append((row, column))
                # Füge die neue Platzierung der Königinnen und die nächste Spalte der Warteschlange hinzu
                queue.append((new_queens, column + 1))
                
    return None

def is_valid(queens, row, column):
    # Gehe alle platzierten Königinnen durch
    for q_row, q_col in queens:
        # Prüfe, ob die neue Königin von einer anderen Königin angegriffen wird
        if q_row == row or q_col == column or abs(row - q_row) == abs(column - q_col):
            return False
    return True

solution = bfs_solve()
for row in range(8):
    board_row = ['.'] * 8
    for queen in solution:
        if queen[0] == row:
            board_row[queen[1]] = 'Q'
    print("".join(board_row))
from collections import deque

def bfs_solve():
    # Initialize the queue with an empty chessboard and the first column
    queue = deque([([], 0)])
    
    while queue:
        # Remove the first element from the queue
        queens, column = queue.popleft()
        
        # If all 8 queens are placed, the problem is solved
        if column == 8:
            return queens

        # Go through all rows of the current column
        for row in range(8):
            # Check if the placement of the queen is valid
            if is_valid(queens, row, column):
                # Create a copy of the current queens and add the new queen
                new_queens = queens.copy()
                new_queens.append((row, column))
                # Add the new placement of queens and the next column to the queue
                queue.append((new_queens, column + 1))
                
    return None

def is_valid(queens, row, column):
    # Go through all placed queens
    for q_row, q_col in queens:
        # Check if the new queen is attacked by another queen
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
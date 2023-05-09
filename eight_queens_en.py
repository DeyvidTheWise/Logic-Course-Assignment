# Initialize the chess board
chess_board = [[0]*8 for _ in range(8)]

# Checks if a queen in the given coordinates (i, j) is under attack
def attack(i, j):
    # Checks for horizontal and vertical attacks
    for k in range(0,8):
        if chess_board[i][k]==1 or chess_board[k][j]==1:
            return True
    # Checks for diagonal attacks
    for k in range(0,8):
        for l in range(0,8):
            if (k+l==i+j) or (k-l==i-j):
                if chess_board[k][l]==1:
                    return True
    return False

# Solves the Eight Queens problem with backtracking and forward checking
def solve(n):
    # If all queens are placed, the problem is solved
    if n==0:
        return True
    # Go through all cells of the chess board
    for i in range(0,8):
        for j in range(0,8):
            # If the cell is not attacked and does not contain a queen
            if (not(attack(i,j))) and (chess_board[i][j]!=1):
                # Place a queen in the cell
                chess_board[i][j] = 1
                # Call the function recursively to place the remaining queens
                if solve(n-1)==True:
                    return True
                # If the placement fails, remove the queen from the cell
                chess_board[i][j] = 0
    return False

# Solve the Eight Queens problem
solve(8)

# Print the resulting chess board
for i in chess_board:
    print(i)
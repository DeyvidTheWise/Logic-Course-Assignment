chess_board = [[0]*8 for _ in range(8)]

def attack(i, j):
    for k in range(0,8):
        if chess_board[i][k]==1 or chess_board[k][j]==1:
            return True
    for k in range(0,8):
        for l in range(0,8):
            if (k+l==i+j) or (k-l==i-j):
                if chess_board[k][l]==1:
                    return True
    return False

def solve(n):
    if n==0:
        return True
    for i in range(0,8):
        for j in range(0,8):
            if (not(attack(i,j))) and (chess_board[i][j]!=1):
                chess_board[i][j] = 1
                if solve(n-1)==True:
                    return True
                chess_board[i][j] = 0
    return False

solve(8)
for i in chess_board:
    print(i)
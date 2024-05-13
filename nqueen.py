n = 4
def printsolution(board): 
    for i in range(n): 
        for j in range(n): 
            print(board[i][j], end = " ")
        print()
def issafe(board, row, col): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 
    for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 
    return True
def solvenqutil(board, col): 
    #basecase 
    if col >= n: 
        return True 
    for i in range(n): 
        if issafe(board, i, col) == True: 
            board[i][col] = 1 
            if solvenqutil(board, col + 1) == True:
                return True 
            board[i][col] = 0 

def solvenq(): 
    board = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    if solvenqutil(board, 0) == False:
        print("Solution doesn't exists") 
        return False
    printsolution(board)
solvenq()
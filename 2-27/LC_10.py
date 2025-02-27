def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for row in board:
        row = [num for num in row if num!='.']
        row_set=set(row)
        if len(row) != len(row_set):
            return False
                 
    for i in range(0,9):
        temp=[]
        for j in range(0,9):
            if board[j][i] != '.':
                temp.append(board[j][i])
        temp_set = set(temp)
        if len(temp) != len(temp_set):
            return False
        
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp=[]
            for n in range(0,3):
                for m in range(0,3):
                   if board[i+n][j+m] != '.':
                        temp.append(board[i+n][j+m])
            temp_set = set(temp)
            if len(temp) != len(temp_set):
                return False
    return True
        
                    
if __name__ == "__main__":
    board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))
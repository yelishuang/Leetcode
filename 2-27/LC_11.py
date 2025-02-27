def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for row in range(n//2):
        for col in range(n):
            temp = matrix[row][col]
            matrix[row][col] = matrix[n-row][col]
            matrix[n-row][col] = temp
    for row in range(n):
        for col in range(row,n):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp 
    return matrix


# 官方题解
def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # method 1
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - 1 - i] = matrix[i][j]
    matrix[:] = matrix_new
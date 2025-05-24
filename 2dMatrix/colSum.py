def printCol(matrix, N, M):
    for i in range(N):
        colsum = 0
        for j in range(M):
            colsum += matrix[j][i]
        print(f"Row {i + 1} sum: {colsum}")

# Example usage:
# Define a matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
N = len(matrix)    # Number of rows
M = len(matrix[0]) # Number of columns
printCol(matrix, N, M)
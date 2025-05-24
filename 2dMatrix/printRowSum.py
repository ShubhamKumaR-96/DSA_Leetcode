# Print row matrix

def printRow(matrix, N, M):
    for i in range(N):
        rowsum = 0
        for j in range(M):
            rowsum += matrix[i][j]
        print(f"Row {i + 1} sum: {rowsum}")

# Define a matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
N = len(matrix)    # Number of rows
M = len(matrix[0]) # Number of columns
printRow(matrix, N, M)
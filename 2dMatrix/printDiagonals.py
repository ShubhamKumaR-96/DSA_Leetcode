# Print diagonals from left to right

def printDiagonals(matrix):
    n=len(matrix)
    for i in range(n):
        print(matrix[i][i],end=" ")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Diagonal elements (left to right):")
printDiagonals(matrix)

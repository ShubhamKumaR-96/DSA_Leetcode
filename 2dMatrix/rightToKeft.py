# print right to left diagonals

def rightToLeft(matrix):
    n=len(matrix)

    for i in range(n):
        print(matrix[i][n-1-i])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Diagonal elements (right to left):")
rightToLeft(matrix)

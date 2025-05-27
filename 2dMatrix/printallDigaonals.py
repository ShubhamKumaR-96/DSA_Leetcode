# Question 4 Print diagonals in a matrix (right to left)
# Problem Statement Given a 2D matrix mat print all the elements diagonally from right to left




def print_diagonal(matrix, start_row, start_col):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    s = start_row
    e = start_col
    while s < n and e >= 0:
        print(matrix[s][e], end=" ")
        s += 1
        e -= 1
    print()

def print_all_diagonals(matrix):
    n = len(matrix)
    if n == 0:
        return
    m = len(matrix[0])

    print("Diagonals starting from first row:")
    for j in range(m):
        print_diagonal(matrix, 0, j)

    print("\nDiagonals starting from last column:")
    for i in range(1, n):
        print_diagonal(matrix, i, m-1)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_all_diagonals(matrix)          
               


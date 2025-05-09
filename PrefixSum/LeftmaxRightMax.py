def getLeftRightMax(A):
    n = len(A)
    leftMax = [0] * n
    rightMax = [0] * n

    # Fill leftMax
    leftMax[0] = A[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], A[i])

    # Fill rightMax
    rightMax[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], A[i])

    return leftMax, rightMax

# Example usage
A = [3, 1, 4, 2, 5]
leftMax, rightMax = getLeftRightMax(A)
print("LeftMax :", leftMax)
print("RightMax:", rightMax)

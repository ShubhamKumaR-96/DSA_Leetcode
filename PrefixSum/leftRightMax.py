# Array of size N. Return 2 arrays leftmax and rightmax  
# Leftmax[i]= max of all elements rom (0-i)
# RightMax[i=>n-1]= max of all elements from i=>n-1  arr= -3 6 2 4 7 2 8 -9 3 1

# Brute force way
# def leftRightMax(A):
#     n=len(A)

#     leftmax=[0]*n
#     rightMax=[0]*n

#     for i in range(1,n):
#         leftmax[i]=max(A[:i+1])

#     for i in range(n):
#         rightMax[i]=max(A[i:])

#     return leftmax,rightMax


# Optimized way using prefix sum (cummulative way)

def rightLeftMaxVal(A):
    n=len(A)

    leftmax=[0]*n
    rightmax=[0]*n

    leftmax[0]=A[0]
    for i in range(1,n):
        leftmax[i]=max(leftmax[i-1],A[i])

    rightmax[n-1]=A[n-1]
    for i in range(n-2,-1,-1):
        rightmax[i]=max(rightmax[i+1],A[i])

    return leftmax,rightmax       

A=list(map(int,input("Enter elements:").split()))
leftmax,rightmax=rightLeftMaxVal(A)
print(f"Left Max : {leftmax}")
print(f"Right max : {rightmax}")
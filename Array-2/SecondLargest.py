# You are given an integer array A. 
# You have to find the second largest element/value in the array or report that no such element exists.

def secMax(A):
    n=len(A)
    firstMax=float('-inf')
    secMax=float('-inf')

    for i in range(n):
        if A[i]>firstMax:
            secMax=firstMax
            firstMax=A[i]
        elif A[i]>secMax and A[i]!=firstMax:
            secMax=A[i]

    return secMax if secMax != float('-inf') else -1 

A=list(map(int,input("Enter list: ").split()))
print(f"sec max : {secMax(A)}")               

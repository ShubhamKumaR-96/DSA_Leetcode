# Print All the subarray

def subArr(A):
    n=len(A)

    for i in range(n):
        for j in range(i,n):
            print(A[i:j+1])

A=[1,2,3,4,5]
subArr(A)            
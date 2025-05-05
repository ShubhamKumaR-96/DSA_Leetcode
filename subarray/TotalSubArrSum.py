# Find sum of all subarrays sums

# using contribution techniques

def subArr(A):
    n=len(A)
    total=0
    for i in range(n):
        total+= A[i] * (i+1) * (n-i)

    return total

A=[3,-2,4-1,2,6]
print(f"Total sum : {subArr(A)}")
# Special Index
# Given an array of size N, count the number of special index in the array. 
# Note: Special Indices are those after removing which, sum of all EVEN indexed 
# elements is equal to sum of all ODD indexed elements.

def specialIdx(A):
    n=len(A)

    evenPf=[0]*n
    oddPf=[0]*n
    evenPf[0]=A[0]
    oddPf[0]=0

    # step -1 bulinding prefix sum
    for i in range(1,n):
        if i%2==0:
            evenPf[i]=evenPf[i-1]+A[i]
            oddPf[i]=oddPf[i-1]

        else:
            oddPf[i]=oddPf[i-1]+A[i]
            evenPf[i]=evenPf[i-1]

    count=0

    # step -2 counting special index 

    for i in range(n):
        left_even=evenPf[i-1] if i > 0 else 0
        left_odd=oddPf[i-1]  if i > 0 else 0

        right_even=oddPf[n-1]-oddPf[i] 
        right_odd=evenPf[n-1]-evenPf[i]

        if left_even+right_even == left_odd+right_odd:
            count+=1
    return count

A=[ 4, 3, 2, 7, 6, -2] 
print(f"Total special index: {specialIdx(A)}")                      
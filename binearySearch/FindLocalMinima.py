# Local Minima in an Array
# Question
# Given an array of N distinct elements, find any local minima in the array
# Local Minima - a no. which is smaller than its adjacent neighbors.  A= [3,6,1,0,9,15,8]

def findLocalMinima(A):
    n=len(A)

    stardIdx=0
    endIdx=n-1

    while stardIdx<=endIdx:
        mid=stardIdx+(endIdx-stardIdx)//2

        if (mid==0 or A[mid]<A[mid-1]) and (mid==n-1 or A[mid]<A[mid+1]):
            return A[mid]
        
        elif mid > 0 and A[mid]<A[mid-1]:
            endIdx=mid-1

        else:
            stardIdx=mid+1

    return -1  

nums = list(map(int,input("Enter the elem:").split()))
print(f"Local Minima : {findLocalMinima(nums)}")          

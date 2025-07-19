# Given a sorted array with distinct elements, search the index of an element k,
#  if k is not present, return -1. 
#  arr = 3	6	9	12	14	19	20	23	25	27


def findK(A,k):
    n=len(A)
    startIdx=0
    endIdx=n-1

    while startIdx<=endIdx:
        mid=startIdx+(endIdx-startIdx)//2
        if A[mid]==k:
            return mid
        elif A[mid]<k:
            startIdx=mid+1
        else:
            endIdx=mid-1

    return -1

A=[3,6,9,12,14,19,20,23,25,27]  
ans=findK(A,k=12)

print(f"Find K : {ans}")                  

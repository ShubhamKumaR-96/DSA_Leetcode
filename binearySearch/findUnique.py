# Every element occurs twice except for 1, find the unique element. 
# Note: Duplicate elements are adjacent to each other but the array is not sorted.
# nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

def findUniqueEle(A):
    n=len(A)

    stardIdx=0
    endIdx=n-1

    while stardIdx<endIdx:
        mid=stardIdx+(endIdx-stardIdx)//2

        if mid%2==1:
            mid-=1

        if A[mid]==A[mid+1]:
            stardIdx=mid+2

        else:
            endIdx=mid

    return A[stardIdx]

nums = list(map(int,input("Enter the elem:").split()))
print(f"Unique Ele: {findUniqueEle(nums)}")
                
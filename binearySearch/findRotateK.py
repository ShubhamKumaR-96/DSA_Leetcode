# Given the array nums sorted in ascending order with distinct elements 
# and rotated at an unknown pivot index, write a function to search for a '
# target value k. If found, return its index, otherwise return -1.'

# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4 (since 0 is at index 4)

def findK(A,k):
    n=len(A)

    left,right=0,n-1

    while left<=right:
        mid=left + (right-left)//2

        if A[mid]==k:
            return mid

        if A[left]<=A[mid]:
            if A[left] <= k <A[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if A[mid] < k <=A[right]:
                left=mid+1
            else:
                right=mid-1
    return -1

nums = [4,5,6,7,0,1,2]
k=0
print(f"Find index: {findK(nums,k)}")





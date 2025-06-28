# 2461. Maximum Sum of Distinct Subarrays With Length K
# Problem Understanding
# We need to find the maximum sum of all possible subarrays of length k in nums where all elements are distinct. If no such subarray exists, return 0.

# Examples:
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15 (Subarray [5,4,2] has distinct elements and max sum)

# Input: nums = [4,4,4], k = 3
# Output: 0 (No subarray with distinct elements)

def findKSum(A,k):
    max_sum=0
    n=len(A)

    for i in range(n-k+1):
        subarray= A[i:i+k]
        if len(set(subarray))==k:
            curr_sum=sum(subarray)
            if curr_sum>max_sum:
                max_sum=curr_sum
    return max_sum

A=[1,5,4,2,9,9,9]
k = 3  
print(f" Max sub Arr : {findKSum(A,k)}")             

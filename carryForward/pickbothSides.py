# Given an integer array A of size N.

# You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4 and array A contains 10 elements then

# You can pick the first four elements or can pick the last four elements or can pick 1 from the front and
#  3 from the back etc. you need to return the maximum possible sum of elements you can pick.


#  A = [5, -2, 3 , 1, 2]
#  B = 3


def pickmaxSum(A,B):

    n=len(A)

    curr_sum=sum(A[:B])
    max_sum=curr_sum

    for i in range(1,B+1):
        curr_sum=curr_sum-A[B-i]+A[-i]
        max_sum=max(curr_sum,max_sum)

    return max_sum   

A = [5, -2, 3 , 1, 2]
B = 3   

print(f"max sum from both side: {pickmaxSum(A,B)}")
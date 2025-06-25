# Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.
#  An element is leader if it is strictly greater than all the elements to its right side.
# NOTE:The rightmost element is always a leader.

def leadersEle(A):
    n=len(A)

    leaders=[]
    max_ele=A[-1]
    leaders.append(max_ele)

    for i in range(n-2,-1,-1):
        if A[i]>max_ele:
            leaders.append(A[i])
            max_ele=A[i]

    leaders.reverse()
    return leaders


A = [16, 17, 4, 3, 5, 2]
print(f"Leaders of array: {leadersEle(A)}")

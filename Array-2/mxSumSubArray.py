# given an array of size n. find & return the max-sum of any subarray
# -2 3 4 -1 5 -10 7

def findMaxSum(A):
    n=len(A)
    max_sum=A[0]
    curr_sum=A[0]


    for i in range(1,n):
        if curr_sum < 0:
            curr_sum=0
        curr_sum=curr_sum+A[i]
        max_sum=max(curr_sum,max_sum)    

    return max_sum

# find start and end index of max sub array 
# 
def findMaxSumLength(A):
    n=len(A)
    max_sum=A[0]
    curr_sum=A[0]
    startIdx=0
    endIdx=0
    tempIdx=0

    for i in range(1,n):
        if curr_sum < 0:
            curr_sum=0
            tempIdx=i
        curr_sum=curr_sum+A[i]

        if curr_sum > max_sum:
            max_sum=curr_sum
            startIdx=tempIdx
            endIdx=i   

    return startIdx,endIdx   

A=list(map(int,input("Enter list: ").split())) 
start_index,end_index=findMaxSumLength(A)
print(f"Start index: {start_index}")
print(f"End index: {end_index}")



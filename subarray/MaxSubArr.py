# find the max subarray sum of length K

# Normal Approach
# def maxSubArr(A,K):
#     n=len(A)
#     mxSum=float('-inf')

#     for i in range(n-K+1):
#         arr_sum=sum(A[i:i+K])
#         if arr_sum>mxSum:
#             mxSum=arr_sum
#     return mxSum   

# Sliding window

def mxSubArrKLen(A,K):
    N=len(A)

    if N<K:
        return "Give valid inputs"  
    
    window_sum=sum(A[:K])
    mxSum=window_sum

    for i in range(N-K):
        window_sum=window_sum-A[i]+A[i+K]
        mxSum=max(mxSum,window_sum)

    return mxSum    

A=list(map(int,input("Enter Element : ").split()))
K=int(input("Enter K :"))   
print(f"Max sum array sum : {mxSubArrKLen(A,K)}")

def findDiffandCnt(A,k):
    left=0
    right=1
    cnt=0

    n=len(A)

    while right<n and left<n:
        diff= A[right]-A[left]

        if diff==k:
            cnt+=1
            left+=1
            right+=1
        elif diff < k:
            right+=1
        elif diff > k:

            left+=1
            if left==right:
                right+=1
    return cnt


nums = list(map(int,input("Enter the elem:").split()))
k=int(input("Enter K : "))
print(f"Total Pairs : {findDiffandCnt(nums,k)}")
                    
             



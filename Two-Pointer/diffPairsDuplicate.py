# count no of pairs have sorted array  distinct element duplicate  A[i]-A[j]==k   
# note i!=j    A=-3 0 1 3 6 8 11 14 18 25 K=5


def cntdifPirs(A,k):
    left=0
    right=1
    n=len(A)

    cnt=0

    while left<n and right<n:
        if left==right:
            right+=1
            continue

        diff=A[right]-A[left]

        if diff==k:
            
            left_cnt=1
            right_cnt=1

            while left+1 < n and A[left]==A[left+1]:
                left_cnt+=1
                left+=1

            while right +1 <n and A[right]==A[right+1]:
                right+=1
                right_cnt+=1

            cnt+=left_cnt*right_cnt
            left+=1
            right+=1
        elif diff < k:
            right+=1
        else:
            left+=1

    return cnt


nums = list(map(int,input("Enter the elem:").split()))
k=int(input("Enter K : "))
print(f"Total Pairs : {cntdifPirs(nums,k)}")                

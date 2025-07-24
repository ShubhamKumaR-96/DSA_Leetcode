# count no of pairs have sorted array  distinct element duplicate  A[i]+A[j]==k    
# note i!=j    A=1 4 4 5 5 5 5 6  6 6 7 11  K=10


def cntPairsinDuplicate(A,k):
    left=0
    right=len(A)-1

    cnt=0

    while left<right:
        curr_sum=A[left]+A[right]

        if curr_sum==k:
            if A[left]==A[right]:
                nums=right-left+1

                cnt+=nums*(nums-1)//2
                break   
            else:
                left_cnt=1
                while left+1 <right and A[left]==A[left+1]:
                    left_cnt+=1
                    left+=1
                
                right_cnt=1
                while right-1 > left and A[right]==A[right-1]:
                    right-=1
                    right_cnt+=1

                cnt+=left_cnt*right_cnt  
                left+=1
                right-=1      

        elif curr_sum < k:
            left+=1
        else:
            right-=1
    return cnt

nums = list(map(int,input("Enter the elem:").split()))
k=int(input("Enter K : "))
print(f"Total Pairs : {cntPairsinDuplicate(nums,k)}")

         






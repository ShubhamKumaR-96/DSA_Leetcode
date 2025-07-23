# Given an array of positive integers. find maximum k such that there is no subarray of 
# length k with sum > B   A=3 2 5 4 6 3 7 2 B=20
def findMaxK(A,b):
    n=len(A)

    left=1
    right=n
    ans=0

    while left<=right:
        mid=left+(right-left)//2
        curr_sum=sum(A[:mid])
        valid=True

        if curr_sum>b:
            valid=False

        else:
            for i in range(mid,n):
                curr_sum+=A[i]-A[i-mid]
                if curr_sum>b:
                    valid=False
                    break

        if valid:
            ans=mid
            left=mid+1
        else:
            right=mid-1

    return ans

nums = list(map(int,input("Enter the elem:").split()))
k=int(input("Enter K : "))
print(f"Find Max K : {findMaxK(nums,k)}")
                        

# Given N stalls at positions A[0], A[1], ..., A[N-1] (sorted in ascending order) and M cows, 
# place each cow in a stall such that the minimum distance between any two cows is maximized.

def findMax(A,m):
    n=len(A)

    left=0
    right=A[-1]-A[0]
    ans=0

    while left<=right:
        mid=left + (right-left)//2
        cow_placed=1
        last_pos=A[0]

        for i in range(1,n):
            if A[i]-last_pos>=mid:
                cow_placed+=1
                last_pos=A[i]

                if cow_placed==m:
                    break

        if cow_placed >=m:
            ans=mid
            left=mid+1

        else:
            right=mid-1

    return ans

nums = list(map(int,input("Enter the elem:").split()))
m=int(input("Enter the no of cows: "))
print(f"Distance : {findMax(nums,m)}")

                    
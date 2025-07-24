# Given sorted array distinct elements count all pairs (i,j) such that A[i]+A[j]==k 
# Note i!=j  A= -3 0 1 3 6 8 11 14 18 25


def countPairs(A,k):
    n=len(A)

    p1=0
    p2=n-1

    cnt=0

    while p1<=p2:
        if A[p1]+A[p2]==k:
            cnt+=1
            p1+=1
            p2-=1
        elif A[p1]+A[p2]<k:
            p1+=1
        else:
            p2-=1
    return cnt


nums = list(map(int,input("Enter the elem:").split()))
k=int(input("Enter K : "))
print(f"Total Pairs : {countPairs(nums,k)}")

    
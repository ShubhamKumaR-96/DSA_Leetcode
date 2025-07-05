# Given an array of size N. You need to tell me count of pairs (i,j),
# such that (a[i]+a[j]%m==0)

def cntPairs(A,K):
    n=len(A)
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if (A[i]+A[j])%K==0:
                cnt+=1

    return cnt

# optimized way
# 
def cntpairsModuleo(A,k):
    n=len(A)
    count=[0]*k
    ans=0

    for i in range(n):
        rem=A[i]%k
        count[rem]+=1

    ans+=count[0]*(count[0]-1)//2

    for i in range(1,k//2+1):
        if i!=k-i:
            ans+=count[i]*(count[k-i])
        else:
          ans+=count[i]*(count[i]-1)//2

    return ans




A=[4,7,6,5,5,3]
k=3
print(f"Total pairs : {cntpairsModuleo(A,k)}")
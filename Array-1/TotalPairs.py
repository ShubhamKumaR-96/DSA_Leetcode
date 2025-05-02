def countPairs(A,k):
    n=len(A)
    cnt=0

    for i in range(n):
        for j in range(i+1,n):
            if A[i]+A[j]==k:
                cnt+=1

    return cnt

A=list(map(int,input("Enter the elements : ").split())) 
K=int(input("Enter K : "))
print(f"Max Element : {countPairs(A,K)}")


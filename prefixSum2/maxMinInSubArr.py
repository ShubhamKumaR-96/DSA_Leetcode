# Array => find smallest subarray length such that it contains both min & max value 
# of the array   Arr= 1 2 3 1 3 4 6 4 6 3

# brute force way O(n^2)
def minMaxValue(A):
    n=len(A)

    maxEle=max(A)
    minEle=min(A)
    ans=n

    for i in range(n):
        if A[i]==maxEle:
            for j in range(i,n):
                if A[j]==minEle:
                    ans=min(ans,j-i+1)

        if A[i]==minEle:
            for j in range(i,n):
                if A[j]==maxEle:
                    ans=min(ans,j-i+1)
    return ans


# OPTIMIZED WAY USING CARRY FORWARD TECHNIQUE T.C O(N)

def minMaxValSubArr(A):
    n=len(A)
    maxEle=max(A)
    minEle=min(A)

    nMax=-1
    nMin=-1
    ans=n

    for i in range(n):
        if A[i]==minEle:
            nMin=i
            if nMax!=-1:
                ans=abs(min(ans,i-nMax+1))
        if A[i]==maxEle:
            nMax=i
            if nMin!=-1:
                ans=abs(min(ans,i-nMin+1))

    return ans                    
    

A=list(map(int,input("Enter elements:").split()))
print(f"min and max value length: {minMaxValSubArr(A)}")
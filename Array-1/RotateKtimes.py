# gIVEN A[N] elements, Rotate this array from last to first for no of times

def revSubArr(A,startidx,endidx):
    n=len(A)

    while startidx<=endidx:
        A[startidx],A[endidx]=A[endidx],A[startidx]
        startidx+=1
        endidx-=1

    return A

def revKtimes(A,k):
    n=len(A)
    K=k%n

    revSubArr(A,0,n-1)
    revSubArr(A,0,K-1)
    revSubArr(A,K,n-1)

    return A

A=list(map(int,input("Enter the elements : ").split())) 
K=int(input("Enter K : "))
print(f"After K time rotating: {revKtimes(A,K)}")


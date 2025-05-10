# Array of size N all the elements are equla to 0
# q=> Queries => add value to all elements from index to n-1

def addValueIndex(A,q):
    n=len(A)

    while q>0:
        Idx=int(input("Enter index: "))
        val=int(input("Enter value: " ))
        for i in range(Idx,n):
            A[i]+=val
        q-=1

    return A

A=list(map(int,input("Enter elements:").split()))
queries=int(input("Enter queries: "))    
Result=addValueIndex(A,queries)
print(f" After queries: {Result}")
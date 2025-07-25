# Inplace sort

def inplaceSort(A):
    n=len(A)

    for i in range(1,n):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key    

    return A

A=[10,6,14,20,2,19]
print(f"Original Arr: {A}")
arr=inplaceSort(A)
print(f"After selection sort: {arr}")         


# Selection Sort

def SelectionSort(A):
    n=len(A)

    for i in range(n):
        minIdx=i
        for j in range(i+1,n):
            if A[j]<A[minIdx]:
                minIdx=j

        A[i],A[minIdx]=A[minIdx],A[i]

    return A   

def stableSelectionSort(A):
    n=len(A)

    for i in range(n):
        minIdx=i
        for j in range(i+1,n):
            if A[j]<A[minIdx] or (A[j]==A[minIdx] and j<minIdx):
                minIdx=j   

        min_val=A[minIdx]
        while minIdx>i:
            A[minIdx]=A[minIdx-1]
            minIdx-=1
        A[i]=min_val

    return A             

 
A=[64, 25, 12, 22,15,25,11]  
print(f"Original Arr: {A}")
list1=stableSelectionSort(A)
print(f"After selection sort: {list1}")           

# Bubble sort

def bubbleSort(A):
    n=len(A)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

    return A


# Modify bubble sort   

def modifyBubbleSort(A):
    n=len(A)

    for i in range(n-1):
        flag=False
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                flag=True

        if not flag:
            break

    return A    





A=[9,3,8,6,7,-2,11,4,5]
print(f"Original Arr: {A}")
arr=modifyBubbleSort(A)
print(f"After selection sort: {arr}")           

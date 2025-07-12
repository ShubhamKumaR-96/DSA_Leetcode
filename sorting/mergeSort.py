# Given 2 sorted arrays merge them and find form of overall subarray
# A : 2 5 7 12 20 24 29
# B : 6 9 10 14 18 19


def mergrTwoArr(A, B):
    i = j = 0
    merge = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merge.append(A[i])
            i += 1
        else:
            merge.append(B[j])
            j += 1

    if i == len(A):
        while j < len(B):
            merge.append(B[j])
            j += 1

    if j == len(B):
        while i < len(A):
            merge.append(A[i])
            i += 1

    return merge



A=[2,5,7,12,20,24,29]
B=[6,9,10,14,18,19]  
mergeArr=mergrTwoArr(A,B)
print("After merging: ",mergeArr)                  

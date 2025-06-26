# Problem 2 : Max And Min
# Given an array of N integers, return the length of smallest subarray which contains
#  both maximum and minimum element of the array. A=[1, 2, 3, 1, 3, 4, 6, 4, 6, 3]

def findClosetMinMax(A):
    n=len(A)

    min_val=min(A)
    max_val=max(A)
    ans=n

    if min_val==max_val:
        return 1

    for i in range(n):
        if A[i]==min_val:
            for j in range(i+1,n):
                if A[j]==max_val:
                   ans=min(ans,j-i+1)
                   break

        if A[i]==max_val:
            for j in range(i+1,n):
                if A[j]==min_val:
                   ans=min(ans,j-i+1)
                   break

    return ans

# Optimized way

def minMaxSub(A):
    n=len(A)

    min_val=min(A)
    max_val=max(A)

    min_index= -1
    max_index= -1
    ans=n

    for i in range(n-1,-1,-1):
        if A[i]==min_val:
            min_index=i
            if max_index!=-1:
                ans=min(ans,max_index-i+1)

        if A[i]==max_val:
            max_index=i
            if min_index!=-1:
                ans=min(ans,max_index-i+1)

    return ans                        

A=[1, 2, 3, 1, 3, 4, 6, 4, 6, 3]  
print(f"Smallest min max SubArr: {minMaxSub(A)}")                        


















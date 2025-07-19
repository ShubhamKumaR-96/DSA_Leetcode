# Given a sorted array of N elements, find the first occurrence of the target element. 
# arr=   -5	-5	-3	0	0	1	1	5	5	5	5	5	5	5	8	10	10	15	15

def firstOcc(A,num):
    n=len(A)

    stardIdx=0
    endIdx=n-1
    idx = -1

    while stardIdx<=endIdx:
        mid = stardIdx + (endIdx-stardIdx)//2
        if A[mid]==num:
            idx=mid
            endIdx=mid-1
        elif A[mid]<num:
            stardIdx=mid+1
        else:
            endIdx=mid-1

    return idx     

A=[-5,-5,-3,0,0,1,1,5,5,5,5,5,5,58,10,10,15,15] 
num=5
print(f"First Occurance idx: {firstOcc(A,num)}")          
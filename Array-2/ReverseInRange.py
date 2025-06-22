# Given an array A of N integers. Also given are two integers B and C.
#  Reverse the array A in the given range [B, C]


def reverseInRange(A,B,C):

    startIdx=B
    endIdx=C

    while startIdx<endIdx:
        A[startIdx],A[endIdx]=A[endIdx],A[startIdx]
        startIdx+=1
        endIdx-=1

    return A 

A = list(map(int,input("Enter the list: ").split()))
B = 2
C = 3
print(f"reverse arr: {reverseInRange(A,B,C)}")
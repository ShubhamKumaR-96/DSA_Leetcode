# Linear Search - Multiple Occurences

# Given an array A and an integer B, find the number of occurrences of B in A.
# Input 1: A = [1, 2, 2], B = 2

# Input 2: A = [1, 2, 1], B = 3

def cntOccurance(A,B):
    cnt=0
    for num in A:
        if num==B:
            cnt+=1
    return cnt

A=list(map(int,input("Enter list: ").split()))
B=int(input("Enter B: "))
print(f"Total occurance: {cntOccurance(A,B)}")


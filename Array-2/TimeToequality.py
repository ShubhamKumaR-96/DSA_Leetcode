# Q4. Time to equality
# Problem Description
# Given an integer array A of size N. In one second, you can increase the value of one element by 1.

# Find the minimum time in seconds to make all elements of the array equal.

def equality(A):
    n=len(A)
    max_ele=max(A)
    time_taken=0
    for i in range(n):
        time_taken+=(max_ele-A[i])
        
    return time_taken


A=list(map(int,input("Enter list: ").split()))
print(f"Total time: {equality(A)}")
        



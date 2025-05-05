# Print all sub array sum

def printAllSubArr(A):
    n=len(A)

    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=A[j]
            print(f"Subarray A[{i}:{j+1}] = {A[i:j+1]}, Sum = {curr_sum}")

A=[3,-2,4-1,2,6]
printAllSubArr(A)
#  Sum of even indexed elements
# Given an array of size N and Q queries with start (s) and end (e) index. For every query, 
# return the sum of all even indexed elements from s to e.

def evenIdxSum(A,s,e):
    n=len(A)

    evenPf=[0]*n
    evenPf[0]=A[0]

    # step - 1 to bulinding prefix sum

    for i in range(1,n):
        if i%2==0:
            evenPf[i]=evenPf[i-1]+A[i]
        else:
            evenPf[i]=evenPf[i-1]

    # step - 2  sum of all even indexed elements from s to e.    

    for i in range(1,n):
        if s==0:
            return evenPf[e]
        if s%2==0:
            return evenPf[e]-evenPf[s-2]
        else:
            return evenPf[e]-evenPf[s-1]

A=[2, 3, 1, 6, 4, 5 ]    
queries = [(1, 3), (2, 5), (0, 4), (3, 3)]   

for s,e in queries:
    print(f"even idx sum from {s} to {e} = {evenIdxSum(A,s,e)}")


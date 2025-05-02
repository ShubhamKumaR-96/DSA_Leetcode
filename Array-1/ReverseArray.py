# Reverse the whole array

def revArr(A):
    n=len(A)

    startIdx=0
    endIdx=n-1

    while startIdx<endIdx:
        A[startIdx],A[endIdx]=A[endIdx],A[startIdx]
        startIdx+=1
        endIdx-=1

    return A    


A=list(map(int,input("Enter the elements : ").split())) 
print(f"Reverse Array : {revArr(A)}")   
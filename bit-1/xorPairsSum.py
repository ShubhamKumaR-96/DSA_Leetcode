# Given an array of non -ve numbers. calculate the size of xor of all possible pairs 
# A =[3,6,5,8]

# Brute force way
def xorSums(A):
    n=len(A)

    result=0

    for i in range(n):
        for j in range(i+1,n):
            result+=(A[i]^A[j])

    return result  


# optimized way
def xorPairsSum(A):
    n=len(A)
    result=0
    for i in range(32):
        count_ones=0
        for num in A:
            if (num>>i) & 1:
                count_ones+=1
        result+=(count_ones*(n-count_ones)*(1<<i))

    return result            



A =[3,6,5,8]
print(f"All possible pairs {xorPairsSum(A)}")          
# Given an array of size N. find the first non repeating elemnent in array
# A : 8 2 8 3 1 2 6 5  o/p=3


def firstOc(A):
    
    freq={}

    for num in A:
        freq[num]=freq.get(num,0)+1

    for num in A:
        if freq[num]==1:
            return num

    return -1

A=[8,2,8,3,1,2,6,5]   
print(f"First non repeating: {firstOc(A)}")     
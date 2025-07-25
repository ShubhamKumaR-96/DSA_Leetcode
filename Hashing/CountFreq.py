# Find unique number of occrance

def uniqueFreq(A):
    n=len(A)

    freq={}

    for num in A:
        freq[num]=freq.get(num,0)+1

    freq_val=freq.values()

    return len(freq_val)==len(set(freq_val))

A=[1,2,2,1,1,3]
print(uniqueFreq(A))    
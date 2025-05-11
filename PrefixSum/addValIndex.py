# Array of size N all the elements are equla to 0
# q=> Queries => add value to all elements from start index to end index

def queriesSum(n, queries):
    A = [0] * n
    diff = [0] * (n + 1)  # Extra space for difference array
    
    while queries > 0:
        startIdx = int(input("Enter startIdx: "))
        endIdx = int(input("Enter endIndex: "))
        val = int(input("Enter the value: "))
        
        diff[startIdx] += val
        if endIdx + 1 < n:
            diff[endIdx + 1] -= val
            
        queries -= 1
    
    # Reconstruct the array 
    A[0] = diff[0]
    for i in range(1, n):
        A[i] = A[i - 1] + diff[i]
    
    return A

n = int(input("Enter array size: "))
queries = int(input("Enter queries: "))
Result = queriesSum(n, queries)
print(f"After queries: {Result}")
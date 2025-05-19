def count_special_index(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    prefix_even = [0] * n
    prefix_odd = [0] * n
    
    prefix_even[0] = arr[0]
    prefix_odd[0] = 0
    
    for i in range(1, n):
        if i % 2 == 0:
            prefix_even[i] = prefix_even[i-1] + arr[i]
            prefix_odd[i] = prefix_odd[i-1]
        else:
            prefix_even[i] = prefix_even[i-1]
            prefix_odd[i] = prefix_odd[i-1] + arr[i]
    
    count = 0
    
    for i in range(n):
        if i == 0:
            sum_even = prefix_odd[n-1] - prefix_odd[i]
            sum_odd = prefix_even[n-1] - prefix_even[i]
        else:
            sum_even = prefix_even[i-1] + (prefix_odd[n-1] - prefix_odd[i])
            sum_odd = prefix_odd[i-1] + (prefix_even[n-1] - prefix_even[i])
        
        if sum_even == sum_odd:
            count += 1
    
    return count

A=list(map(int,input("Enter elements:").split()))
print(f"SpeciaL iNDEX : {count_special_index(A)}")
# Find equlibrium index

def findEquilibriumIndex(nums):
    total_sum = sum(nums)  
    left_sum = 0  
    
    for i in range(len(nums)):  
        if left_sum == total_sum - left_sum - nums[i]:  # Equilibrium condition
            return i  # Return index
        left_sum += nums[i]  
    
    return -1  # If no equilibrium index found

# Example usage
nums = [-7, 1, 5, 2, -4, 3, 0]
print(f"Equilibrium Index: {findEquilibriumIndex(nums)}")
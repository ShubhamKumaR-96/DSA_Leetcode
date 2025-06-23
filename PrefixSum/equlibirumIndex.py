# Find equlibrium index

def findEquilibriumIndex(nums):
    n=len(nums)
    left_sum=0
    right_sum=0

    pf=[0]*n
    pf[0]=nums[0]

    for i in range(1,n):
        pf[i]=pf[i-1]+nums[i]


    for i in range(n):
        if i==0:
            left_sum=0
        else:
            left_sum=pf[i-1]    
        right_sum=pf[n-1]-pf[i]

        if left_sum==right_sum:
            return i
    return -1        
            


# Example usage
nums = [-7, 1, 5, 2, -4, 3, 0]
print(f"Equilibrium Index: {findEquilibriumIndex(nums)}")
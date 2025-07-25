# Given an array of size N. Check if there exits a sub array with sum==0
# A: 2 2 1 -3 4 3 1 -2 -3 

def checkSubArr(A):

    prefix_sum=0
    sum_set=set()

    for num in A:
        prefix_sum+=num

        if prefix_sum==0 or prefix_sum in sum_set:
            return True
        
        sum_set.add(prefix_sum)

    return -1

nums=list(map(int,input("Enter nums: ").split()))   
print(checkSubArr(nums)) 
        
        
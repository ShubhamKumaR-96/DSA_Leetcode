# 3162. Find the Number of Good Pairs I

# Brute force way
def goodPair(num1,num2,k):
    n=len(num1)
    m=len(num2)
    cnt=0

    for i in range(n):
        for j in range(n):
            if num1[i] % (num2[j]*k )== 0:
                cnt+=1

    return cnt

nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1  
print(f"Total Pairs : {goodPair(nums1,nums2,k)}")          

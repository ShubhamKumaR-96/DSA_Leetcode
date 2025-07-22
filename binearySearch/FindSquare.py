# Problem 2 Finding the square root of a number

def findSqureRoot(n):
    if n==0 or n==1:
        return n
    
    startidx=1
    endIdx=n 
    ans=-1

    while startidx<=endIdx:
        mid=startidx + (endIdx-startidx)//2

        mid_squre=mid*mid

        if mid_squre < n:
            ans=mid
            startidx=mid+1

        else:
            endIdx=mid-1

    return ans

n=int(input("Enter N : "))

print(f"Find Nearest Val : {findSqureRoot(n)}")        
                

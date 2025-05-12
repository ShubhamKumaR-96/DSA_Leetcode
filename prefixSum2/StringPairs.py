# Given String S find count pairs (i,j) such that i<j && S[i]=='a' and S[j]=='g'
# S= a b c g a g 

# Brute force way T.c O(N^2)
def cntStringPairs(S):
    n=len(S)
    cnt=0

    for i in range(n):
        for j in range(i+1,n):
            if S[i]=='a' and S[j]=='g':
                cnt+=1

    return cnt


# Optimized way

def cntPairs(S):
    n=len(S)
    cnt=0
    ans=0

    for i in range(n-1,-1,-1):
        if S[i]=='g':
            cnt+=1
        if S[i]=='a':
            ans+=cnt
    return ans

A=list(input("Enter a string:").split())
print(f"Total String Pairs: {cntPairs(A)}")            